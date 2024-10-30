CC       := clang
RM       := rm -f
CHMOD    := chmod +x
FIND     := find
MKDIR    := mkdir -p

CFLAGS   := -Ofast

SRCDIR   := .
INCLUDEDIR := ../libs/clap/include
OUTDIR   := ../type_defs

PARSE_ENUM         := $(SRCDIR)/parse_clap_enums

ENUM_OUTPUT        := $(OUTDIR)/clap_enums.py
DEFINITIONS_OUTPUT := $(OUTDIR)/clap_defs.py
EXTENSIONS_OUTPUT  := $(OUTDIR)/clap_extensions.py

# Header files (generated using find)
HEADER_FILES := $(shell $(FIND) $(INCLUDEDIR) -type f -name "*.h")

.PHONY: all clean enum definitions extensions

all: enum definitions extensions

enum: $(ENUM_OUTPUT)

definitions: $(DEFINITIONS_OUTPUT)

extensions: $(EXTENSIONS_OUTPUT)

$(PARSE_ENUM): $(SRCDIR)/parse_clap_enums.c
	@$(CC) $(CFLAGS) $< -o $@

$(ENUM_OUTPUT): $(PARSE_ENUM) $(HEADER_FILES)
	@$(MKDIR) $(OUTDIR)
	@$(PARSE_ENUM) enum $(HEADER_FILES) > $@

$(DEFINITIONS_OUTPUT): $(PARSE_ENUM) $(HEADER_FILES)
	@$(MKDIR) $(OUTDIR)
	@$(PARSE_ENUM) def $(HEADER_FILES) > $@

$(EXTENSIONS_OUTPUT): $(PARSE_ENUM) $(HEADER_FILES)
	@$(MKDIR) $(OUTDIR)
	@$(PARSE_ENUM) ext $(HEADER_FILES) > $@

clean:
	$(RM) $(PARSE_ENUM) $(PARSE_DEFINITIONS) $(PARSE_EXTENSIONS)
	$(RM) $(ENUM_OUTPUT) $(DEFINITIONS_OUTPUT) $(EXTENSIONS_OUTPUT)