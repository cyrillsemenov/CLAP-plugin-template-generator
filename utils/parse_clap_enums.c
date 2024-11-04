#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define TOOLNAME "CLAP Data Parser"

#define MIN_MEMBERS 2 // TODO: Handle singe member enums

#define ENUM "enum "
#define DEFINE "#define"
#define BLOCK_OPEN '{'
#define BLOCK_CLOSE '}'
#define COMMENT "// "
#define CONSTEXPR "static CLAP_CONSTEXPR const char "
#define PORT_PREFIX "CLAP_PORT_"
#define EXT_PREFIX "CLAP_EXT_"
#define CONSTEXPR_DELIM "[] = "

#define ENUM_DATA 0
#define ENUM_ENTRY 1

#define MAX_PREFIX_WORDS 100

#ifdef PRINT_VALUES
#    undef PRINT_VALUES
#    define PRINT_VALUES(k, v) fprintf(stderr, "- %-40s: %s\n", k, v)
#else
#    define PRINT_VALUES(k, v)
#endif

#define STARTS_WITH(line, char)                                                \
    if (*line != char)                                                         \
        continue;

#define TRIM_SPACE(line)                                                       \
    while (isspace(*line))                                                     \
        line++;

#define CLEAR_STR(buf) buf[0] = '\0'

typedef struct enum_entry {
    char *name;              // Entry name after trimming common prefix
    char *c_name;            // Original C name of the entry
    char *value;             // Optional value for the entry
    char *description;       // Description/comment for the entry
    struct enum_entry *next; // Pointer to the next entry
} enum_entry_t;

typedef struct enum_data {
    char *name;             // Name of the enum
    char *filename;         // Source filename (if needed)
    char *comment;          // Comment describing the enum
    enum_entry_t *entries;  // Linked list of enum entries
    struct enum_data *next; // Pointer to the next enum
    size_t entries_num;     // Size of entries list
} enum_data_t;

enum_entry_t *enum_entry_init(const char *name, const char *value,
                              const char *description);
void enum_entry_destroy(enum_entry_t *entry);

void parse_directory(const char *path, const char *ignore);
void parse_enum(char *path);
void parse_defs(char *path);
void parse_extensions(char *path);
static enum_data_t *plugin_extensions_enum = NULL;
static enum_entry_t *last_plugin_extensions_entry = NULL;
static enum_data_t *host_extensions_enum = NULL;
static enum_entry_t *last_host_extensions_entry = NULL;
static enum_data_t *port_types_enum = NULL;
static enum_entry_t *last_port_types_entry = NULL;

char *construct_name_from_path(const char *path);
static inline enum_data_t *enum_data_init(const char *name, const char *path,
                                          const char *comment);
static inline void enum_data_destroy(enum_data_t *enum_data);
static inline const char *now();
static inline void print_indented(const char *str, int indent_level);
static inline void print_comment(void *e, unsigned int type);
static inline void camel_to_pascal(char *str);
static inline size_t common_prefix(enum_data_t *enum_data, char **prefix,
                                   const char separator);
static inline void print_file_header(const char *tool_name);
static inline void print_enum(enum_data_t *cur, size_t min_members);

int main(int argc, char *argv[]) {
    if (argc < 3) {
        fprintf(stderr, "Usage: %s [ enum | def | ext ] [path]\n", argv[0]);
        return 1;
    }

    int opt = -1;

    if (strcmp(argv[1], "enum") == 0) {
        opt = 0;
    } else if (strcmp(argv[1], "def") == 0) {
        opt = 1;
    } else if (strcmp(argv[1], "ext") == 0) {
        opt = 2;
    } else {
        fprintf(stderr, "Usage: %s [ enum | def | ext ] [path]\n", argv[0]);
        return 1;
    }

    print_file_header(TOOLNAME);

    int i = 1;
    while (i++ < argc - 1) {
        fprintf(stderr, "Processing file '%s'...\n", argv[i]);
        switch (opt) {
            case 0:
                parse_enum(argv[i]);
                break;
            case 1:
                parse_defs(argv[i]);
                break;
            case 2:
                if (!plugin_extensions_enum)
                    plugin_extensions_enum =
                        enum_data_init("clap_plugin_extensions", NULL,
                                       "CLAP plugin extensions\n");
                if (!host_extensions_enum)
                    host_extensions_enum = enum_data_init(
                        "clap_host_extensions", NULL, "CLAP host extensions\n");
                if (!port_types_enum)
                    port_types_enum =
                        enum_data_init("clap_audio_port_type", NULL,
                                       "CLAP audio port types\n");
                parse_extensions(argv[i]);
                break;
        }
    }

    if (opt == 2) {
        if (port_types_enum) {
            print_enum(port_types_enum, MIN_MEMBERS);
            enum_data_destroy(port_types_enum);
        }
        if (plugin_extensions_enum) {
            print_enum(plugin_extensions_enum, MIN_MEMBERS);
            enum_data_destroy(plugin_extensions_enum);
        }
        if (host_extensions_enum) {
            print_enum(host_extensions_enum, MIN_MEMBERS);
            enum_data_destroy(host_extensions_enum);
        }
    }

    return 0;
}

void parse_enum(char *path) {
    FILE *file = fopen(path, "r");

    char line[256];

    if (!file) {
        fprintf(stderr, "Unable to open file '%s'!\n", path);
        return;
    }

    enum_data_t *current_enum = NULL;
    enum_entry_t *last_entry = NULL;
    char comment_buffer[UINT16_MAX];

    while (fgets(line, sizeof(line), file)) {
        char *ptr = line;

        TRIM_SPACE(ptr);
        if (strlen(ptr) == 0) {
            // Clear comment buffer on empty line
            CLEAR_STR(comment_buffer);
            continue;
        }

        // Check if it is commented line
        if (strncmp(ptr, COMMENT, strlen(COMMENT) - 1) == 0) {
            // For emty comment line just append a newline to comment buffer
            if (strlen(ptr) <= strlen(COMMENT)) {
                strcat(comment_buffer, "\n");
                continue;
            }
            // Store comment text
            ptr += strlen(COMMENT);
            strcat(comment_buffer, ptr);
            continue;
        }

        char *enum_end = strchr(ptr, BLOCK_CLOSE);

        if (!current_enum) {
            if (strncmp(ptr, ENUM, strlen(ENUM)) != 0)
                continue;
            // enter enum
            char *enum_name = ptr + strlen(ENUM);

            // find name between enum entry and this point (can be empty)
            char *enum_name_end = strchr(enum_name, BLOCK_OPEN);
            if (enum_name_end) {
                *enum_name_end = '\0';
                enum_name_end++;
            }
            ptr = enum_name_end;
            TRIM_SPACE(ptr);

            char comment[UINT16_MAX] = "";
            sprintf(comment, "File: %s\n", path);

            if (strlen(comment_buffer)) {
                // Handle enum comment
                strcat(comment, "\n");
                strcat(comment, comment_buffer);
                CLEAR_STR(comment_buffer);
            }

            current_enum = enum_data_init(enum_name, path, comment);
        }

        if (current_enum) {

            if (enum_end) {
                CLEAR_STR(comment_buffer);
                // handle single lined enum
                *enum_end = '\0';
                // remove trailing spaces
                char *end = ptr + strlen(ptr) - 1;
                while (end >= ptr && isspace((unsigned char)*end)) {
                    *end = '\0';
                    end--;
                }
            }
            char *entry_name = ptr;
            char *value = strstr(ptr, " = "); // find value
            char *eol = strchr(ptr, ',');     // find end of the line
            char *inline_comment = strstr(ptr, "// ");

            if (value) {
                *value = '\0';
                value += strlen(" = ");
            }

            if (eol)
                *eol = '\0';

            if (inline_comment)
                inline_comment += strlen("// ");
            if (strlen(entry_name)) {
                enum_entry_t *new_entry = enum_entry_init(
                    entry_name, value,
                    strlen(comment_buffer) ? comment_buffer : inline_comment);
                // Add the entry to the current enum
                if (last_entry) {
                    (last_entry)->next = new_entry;
                } else {
                    current_enum->entries = new_entry;
                }
                last_entry = new_entry;
                current_enum->entries_num++;

                PRINT_VALUES(last_entry->name, last_entry->description);
            }
        }

        if (enum_end) {
            print_enum(current_enum, MIN_MEMBERS);
            enum_data_destroy(current_enum);
            current_enum = NULL;
            last_entry = NULL;
        }
    }

    fclose(file);
    CLEAR_STR(comment_buffer);

    if (current_enum) {
        fprintf(
            stderr,
            "Something gone terribly wrong and enum %s from file %s was lost\n",
            current_enum->name, current_enum->filename);
        free(current_enum);
    }
}

char *construct_name_from_path(const char *path) {
    if (path == NULL) {
        return NULL;
    }

    // Find the last '/' to separate the folder path and filename
    const char *last_slash = strrchr(path, '/');
    const char *filename_with_ext = last_slash ? last_slash + 1 : path;

    // Extract folder name
    char *folder = NULL;
    if (last_slash && last_slash != path) {
        const char *second_last_slash = last_slash;
        while (second_last_slash > path && *(second_last_slash - 1) != '/') {
            second_last_slash--;
        }
        size_t folder_length = last_slash - second_last_slash;
        folder = (char *)malloc(folder_length + 1);
        if (folder == NULL) {
            return NULL;
        }
        strncpy(folder, second_last_slash, folder_length);
        folder[folder_length] = '\0';
    }

    // Find the last dot to separate the filename and extension
    const char *last_dot = strrchr(filename_with_ext, '.');
    size_t filename_length = last_dot ? (size_t)(last_dot - filename_with_ext)
                                      : strlen(filename_with_ext);

    // Extract filename
    char *filename = (char *)malloc(filename_length + 1);
    if (filename == NULL) {
        free(folder);
        return NULL;
    }
    strncpy(filename, filename_with_ext, filename_length);
    filename[filename_length] = '\0';

    // Construct the new name
    size_t name_length =
        strlen(folder) + strlen(filename) + 2; // 1 for '_', 1 for '\0'
    char *name = (char *)malloc(name_length);
    if (name != NULL) {
        if (folder) {
            strcat(name, folder);
            strcat(name, "_");
        }
        strcat(name, filename);
    }

    // Clean up
    if (folder)
        free(folder);
    free(filename);

    return name; // Caller is responsible for freeing the returned string
}

void parse_defs(char *path) {
    FILE *file = fopen(path, "r");

    char line[256];

    if (!file) {
        fprintf(stderr, "Unable to open file '%s'!\n", path);
        return;
    }

    enum_data_t *current_enum = NULL;
    enum_entry_t *last_entry = NULL;
    char comment_buffer[UINT16_MAX];

    while (fgets(line, sizeof(line), file)) {
        char *ptr = line;

        STARTS_WITH(ptr, '#');

        // We look for unconditional defines only.
        // Fortunately, CLAP formatting allows us to distinguish them,
        // as conditional defines are indented.
        if (strncmp(ptr, DEFINE, strlen(DEFINE)) != 0) {
            continue;
        }
        ptr += strlen(DEFINE);

        TRIM_SPACE(ptr);

        char *key = ptr;
        // Find the space separating the macro name and value
        char *value = strchr(ptr, ' ');
        if (!value)
            continue;

        // Skip function-like macros
        char *open_parenthesis = strchr(ptr, '(');
        if (open_parenthesis && open_parenthesis < value)
            continue;

        // Skip muliline macros fon now
        if (strrchr(value, '\\'))
            continue;

        // Null-terminate the macro name and advance to the value
        *value = '\0';
        value++;
        TRIM_SPACE(value);

        if (!current_enum) {
            current_enum =
                enum_data_init(construct_name_from_path(path), path, NULL);
            // inside_enum = true;
            // start_enum_parsing(path);
        }

        if (current_enum) {
            PRINT_VALUES(key, value);
            enum_entry_t *new_entry = enum_entry_init(key, value, value);
            // Add the entry to the current enum
            if (last_entry) {
                (last_entry)->next = new_entry;
            } else {
                current_enum->entries = new_entry;
            }
            last_entry = new_entry;
            current_enum->entries_num++;
        }
    }
    if (current_enum) {
        print_enum(current_enum, MIN_MEMBERS);
        enum_data_destroy(current_enum);
        current_enum = NULL;
        last_entry = NULL;
    }
    fclose(file);
}

enum_entry_t *enum_entry_copy(enum_entry_t *src) {
    if (!src)
        return NULL;

    enum_entry_t *dst =
        enum_entry_init(src->name, src->value, src->description);
    if (!dst) {
        fprintf(stderr, "Memory allocation failed.\n");
        return NULL;
    }

    dst->next = enum_entry_copy(src->next);

    return dst;
}

void parse_extensions(char *path) {
    FILE *file = fopen(path, "r");

    char line[256];

    if (!file) {
        fprintf(stderr, "Unable to open file '%s'!\n", path);
        return;
    }

    char comment_buffer[UINT16_MAX];
    bool plugin_extensions = false;
    bool host_extensions = false;
    enum_entry_t *file_extensions = NULL;
    enum_entry_t *file_extensions_head = file_extensions;
    size_t extensions_num = 0;

    while (fgets(line, sizeof(line), file)) {
        char *ptr = line;

        if (strlen(ptr) == 0) {
            // Clear comment buffer on empty line
            CLEAR_STR(comment_buffer);
            continue;
        }

        // Parse comments before declaration
        if (strncmp(ptr, COMMENT, strlen(COMMENT) - 1) == 0) {
            // For emty comment line just append a newline to comment buffer
            if (strlen(ptr) <= strlen(COMMENT)) {
                strcat(comment_buffer, "\n");
                continue;
            }
            // Store comment text
            ptr += strlen(COMMENT);
            strcat(comment_buffer, ptr);
            continue;
        }

        if (strncmp(ptr, "} clap_host_", strlen("} clap_host_")) == 0) {
            host_extensions = true;
            comment_buffer[0] = '\0';
            continue;
        }

        if (strncmp(ptr, "} clap_plugin_", strlen("} clap_plugin_")) == 0) {
            plugin_extensions = true;
            comment_buffer[0] = '\0';
            continue;
        }

        // Check line length
        if (*ptr != CONSTEXPR[0] || strlen(ptr) <= strlen(CONSTEXPR)) {
            comment_buffer[0] = '\0';
            continue;
        }

        // Start declaration parsing
        if (strncmp(ptr, CONSTEXPR, strlen(CONSTEXPR)) != 0) {
            comment_buffer[0] = '\0';
            continue;
        }
        ptr += strlen(CONSTEXPR);
        char *entry_name = ptr;

        char *val = strstr(ptr, CONSTEXPR_DELIM);
        if (!val) {
            comment_buffer[0] = '\0';
            continue;
        }
        val[0] = '\0';
        val += strlen(CONSTEXPR_DELIM);

        char *semicolon = strchr(val, ';');
        if (semicolon)
            *semicolon = '\0';

        PRINT_VALUES(ptr, val);

        char comment[1024] = "";
        sprintf(comment, "File: %s\n\nValue: %s\n", path, val);
        if ((void *)comment_buffer && strlen(comment_buffer) > 0) {
            strcat(comment, "\n");
            strcat(comment, comment_buffer);
        }
        comment_buffer[0] = '\0';

        // Process extension port types
        if (strncmp(ptr, PORT_PREFIX, strlen(PORT_PREFIX)) == 0) {
            enum_entry_t *new_entry = enum_entry_init(entry_name, val, comment);
            if (last_port_types_entry) {
                last_port_types_entry->next = new_entry;
            } else {
                port_types_enum->entries = new_entry;
            }
            last_port_types_entry = new_entry;
            port_types_enum->entries_num++;
        }

        // Process extension declarations
        if (strncmp(ptr, EXT_PREFIX, strlen(EXT_PREFIX)) == 0) {
            enum_entry_t *new_entry = enum_entry_init(entry_name, val, comment);

            if (file_extensions_head) {
                file_extensions_head->next = new_entry;
            } else {
                file_extensions = new_entry;
            }
            file_extensions_head = new_entry;
            extensions_num++;
        }
    }
    fclose(file);
    if (!file_extensions)
        return;

    if (plugin_extensions) {
        enum_entry_t *file_plugin_extensions = enum_entry_copy(file_extensions);
        if (last_plugin_extensions_entry) {
            (last_plugin_extensions_entry)->next = file_plugin_extensions;
        } else {
            plugin_extensions_enum->entries = file_plugin_extensions;
        }
        last_plugin_extensions_entry = file_plugin_extensions;
        plugin_extensions_enum->entries_num += extensions_num;
    }

    if (host_extensions) {
        enum_entry_t *file_host_extensions = enum_entry_copy(file_extensions);
        if (last_host_extensions_entry) {
            (last_host_extensions_entry)->next = file_host_extensions;
        } else {
            host_extensions_enum->entries = file_host_extensions;
        }
        last_host_extensions_entry = file_host_extensions;
        host_extensions_enum->entries_num += extensions_num;
    }
    enum_entry_destroy(file_extensions);
}

enum_entry_t *enum_entry_init(const char *name, const char *value,
                              const char *description) {
    enum_entry_t *new_entry = (enum_entry_t *)calloc(1, sizeof(enum_entry_t));
    if (!new_entry) {
        perror("enum_data_init");
        exit(1);
    }
    new_entry->name = strdup(name);
    if (value && strlen(value) > 0)
        new_entry->value = strdup(value);
    if (description && strlen(description) > 0)
        new_entry->description = strdup(description);
    new_entry->next = NULL;
    return new_entry;
}

void enum_entry_destroy(enum_entry_t *entry) {
    if (!entry)
        return;
    if (entry->name)
        free(entry->name);
    if (entry->value)
        free(entry->value);
    if (entry->description)
        free(entry->description);
    if (entry->next)
        // Hello, stack overflow!
        enum_entry_destroy(entry->next);
    free(entry);
}

static inline enum_data_t *enum_data_init(const char *name, const char *path,
                                          const char *comment) {
    enum_data_t *new_enum = (enum_data_t *)calloc(1, sizeof(enum_data_t));
    if (!new_enum) {
        perror("enum_data_init");
        exit(1);
    }
    if (name && strlen(name) > 0)
        new_enum->name = strdup(name);
    if (path && strlen(path) > 0)
        new_enum->filename = strdup(path);
    if (comment && strlen(comment) > 0)
        new_enum->comment = strdup(comment);
    new_enum->entries = NULL;
    new_enum->next = NULL;
    new_enum->entries_num = 0;
    return new_enum;
}

static inline void enum_data_destroy(enum_data_t *enum_data) {
    if (!enum_data)
        return;
    if (enum_data->name)
        free(enum_data->name);
    if (enum_data->filename)
        free(enum_data->filename);
    if (enum_data->comment)
        free(enum_data->comment);
    enum_entry_destroy(enum_data->entries);
    enum_data_destroy(enum_data->next);
    free(enum_data);
}

static inline const char *now() {
    static char now[17];
    time_t t = time(NULL);
    struct tm tm = *localtime(&t);
    snprintf(now, 17, "%d-%02d-%02d %02d:%02d", tm.tm_year + 1900,
             tm.tm_mon + 1, tm.tm_mday, tm.tm_hour, tm.tm_min);
    return now;
}

static inline void print_indented(const char *str, int indent_level) {
    const char *indent = "    "; // Four spaces for each indentation level
    const char *p = str;
    int i;

    while (*p) {
        // Print indentation
        for (i = 0; i < indent_level; i++) {
            printf("%s", indent);
        }

        // Print characters until the next newline or end of string
        while (*p && *p != '\n') {
            putchar(*p);
            p++;
        }

        // If at a newline, print it and advance the pointer
        if (*p == '\n') {
            putchar('\n');
            p++;
        } else {
            break;
        }
    }
}

static inline void print_comment(void *e, unsigned int type) {
    char *comment;
    if (!e)
        return;
    switch (type) {
        case ENUM_DATA: {
            comment = ((enum_data_t *)e)->comment;
            break;
        }
        case ENUM_ENTRY: {
            comment = ((enum_entry_t *)e)->description;
            break;
        }
        default:
            return;
    }

    if (comment == NULL || strlen(comment) < 2)
        return;

    printf("    \"\"\"\n");
    print_indented(comment, 1);
    printf("    \"\"\"\n\n");
}

static inline void camel_to_pascal(char *str) {
    bool capitalize = true;
    char *src = str;
    char *dest = str;

    while (*src) {
        if (*src == '_' || *src == '-' || *src == ' ') {
            capitalize = true;
        } else {
            if (capitalize) {
                *dest = toupper(*src);
                capitalize = false;
            } else {
                *dest = tolower(*src);
                // *dest = *src;
            }
            dest++;
        }
        src++;
    }
    *dest = '\0';
}

static inline size_t common_prefix(enum_data_t *enum_data, char **prefix,
                                   const char separator) {
    // Do not process empty lists or lists with only one member
    if (!enum_data || !enum_data->entries || !enum_data->entries->next) {
        fprintf(stderr, "Not enough entries for common prefix calculation.\n");
        return 0;
    }

    enum_entry_t *current = enum_data->entries;
    char *common_prefix = strdup(current->name);
    if (!common_prefix) {
        fprintf(stderr, "Memory allocation failed.\n");
        return 0;
    }

    char *sep_pos = strrchr(common_prefix, separator);
    if (!sep_pos || sep_pos == common_prefix) {
        fprintf(stderr, "No separator was foud.\n");
        free(common_prefix);
        return 0;
    }
    *sep_pos = '\0';

    size_t prefix_len = strlen(common_prefix);

    current = current->next;
    while (current) {
        if (!current->name) {
            fprintf(stderr, "An entry has no name.\n");
            free(common_prefix);
            return 0;
        }

        // This loops forever
        while (prefix_len > 0 &&
               strncmp(common_prefix, current->name, prefix_len) != 0) {
            if (!(sep_pos = strrchr(common_prefix, separator))) {
                prefix_len = 0;
                break;
            }
            prefix_len = sep_pos - common_prefix;
            common_prefix[prefix_len] = '\0';
        }

        if (!prefix_len) {
            free(common_prefix);
            *prefix = NULL;
            return 0;
        }

        current = current->next;
    }

    *prefix = common_prefix;
    return prefix_len + 1;
}

static inline void print_file_header(const char *tool_name) {
    printf("\"\"\"\n"
           "This file was automatically generated from CLAP API headers\n"
           "by '%s' tool\n"
           "\n"
           "CLAP: https://github.com/free-audio/clap/\n"
           "%s: "
           "https://github.com/cyrillsemenov/CLAP-plugin-template-generator/"
           "utils/%s\n"
           "\n"
           "Date: %s\n"
           "\"\"\"\n"
           "\n"
           "from enum import StrEnum\n"
           "\n",
           tool_name, tool_name, __FILE_NAME__, now());
}

static inline void print_enum(enum_data_t *cur, size_t min_members) {
    if (!cur)
        return;
    if (cur->entries_num < min_members) {
        cur = cur->next;
        return;
    }
    enum_entry_t *e = cur->entries;
    char *prefix = NULL;
    size_t prefix_len = common_prefix(cur, &prefix, '_');

    if (prefix && !cur->name) {
        cur->name = strdup(prefix);
    }
    // Print class header
    camel_to_pascal(cur->name);
    printf("\nclass %s(StrEnum):\n", cur->name);
    print_comment(cur, ENUM_DATA);

    // Print members
    while (e) {
        printf("    %s = \"%s\"\n", e->name + prefix_len, e->name);
        print_comment(e, ENUM_ENTRY);
        e = e->next;
    }
    printf("\n");
    if (prefix)
        free(prefix);
}
