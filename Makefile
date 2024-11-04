# Simplified Makefile equivalent to the CMakeLists.txt configuration
CC = clang
RM = rm -f

# Project Directories
SRC_DIR = test_src
BUILD_DIR = build
OUTPUT_DIR = $(BUILD_DIR)/$(PROJECT_NAME).clap/Contents/MacOS
LIBS_DIR = libs/clap
INCLUDE_DIRS = -Iinclude -Isrc/include -I$(LIBS_DIR)/include -isysroot $(shell xcrun --show-sdk-path)

# Project Name
PROJECT_NAME = plugin

# Compiler Flags
CFLAGS = -fPIC -Wall -Wextra -pedantic -Werror=pragma-pack
# LDFLAGS = -framework CoreFoundation -framework AppKit -framework CoreGraphics -framework AudioToolbox -framework Cocoa -framework IOKit -framework Carbon -isysroot $(shell xcrun --show-sdk-path)

LDFLAGS_MAC = -framework CoreFoundation -framework AppKit -framework CoreGraphics -framework AudioToolbox -framework Cocoa -framework IOKit -framework Carbon -exported_symbols_list $(SRC_DIR)/macos-symbols.txt
LDFLAGS = -framework CoreFoundation -framework AppKit -framework CoreGraphics -framework AudioToolbox -framework Cocoa -framework IOKit -framework Carbon -exported_symbols_list $(SRC_DIR)/macos-symbols.txt
LDFLAGS_LINUX = -shared -fPIC -Wl,--version-script=$(SRC_DIR)/linux-my_plug.version -Wl,-z,defs
LDFLAGS_WINDOWS = -shared -Wl,--out-implib,$(BUILD_DIR)/$(PROJECT_NAME).a -lws2_32 -lwinmm


# if(CMAKE_SYSTEM_NAME STREQUAL "Linux")
#         target_link_libraries(clap-plugin-template PRIVATE -Wl,--version-script=${CMAKE_CURRENT_SOURCE_DIR}/src/linux-my_plug.version)
#         target_link_libraries(clap-plugin-template PRIVATE -Wl,-z,defs)
#         set_target_properties(clap-plugin-template PROPERTIES SUFFIX ".clap" PREFIX "")
# elseif(CMAKE_SYSTEM_NAME STREQUAL "Darwin")
# 	target_link_options(clap-plugin-template PRIVATE -exported_symbols_list ${CMAKE_CURRENT_SOURCE_DIR}/src/macos-symbols.txt)

# 	set_target_properties(clap-plugin-template PROPERTIES
# 				BUNDLE True
# 				BUNDLE_EXTENSION clap
# 				MACOSX_BUNDLE_GUI_IDENTIFIER com.my_company.my_plug
# 				MACOSX_BUNDLE_BUNDLE_NAME my_plug
# 				MACOSX_BUNDLE_BUNDLE_VERSION "1"
# 				MACOSX_BUNDLE_SHORT_VERSION_STRING "1"
# 				MACOSX_BUNDLE_INFO_PLIST ${CMAKE_CURRENT_SOURCE_DIR}/src/plugins.plist.in
# 				)
# elseif(CMAKE_SYSTEM_NAME STREQUAL "Windows")
# 	set_target_properties(clap-plugin-template PROPERTIES SUFFIX ".clap" PREFIX "")
# endif()

# Sources
SOURCES = $(shell find $(SRC_DIR) -name '*.c')
OBJECTS = $(patsubst $(SRC_DIR)/%.c, $(BUILD_DIR)/%.o, $(SOURCES))

# Default target
.PHONY: all clean install
all: $(OUTPUT_DIR)/$(PROJECT_NAME)

# Clean the build
clean:
	$(RM) -r $(BUILD_DIR)

# Compile object files
$(BUILD_DIR)/%.o: $(SRC_DIR)/%.c
	@mkdir -p $(dir $@)
	$(CC) -c $< -o $@ $(CFLAGS) $(INCLUDE_DIRS)

# Link the final executable as a bundle (for macOS)
$(OUTPUT_DIR)/$(PROJECT_NAME): $(OBJECTS)
	@mkdir -p $(OUTPUT_DIR)
	$(CC) -shared $^ -o $@ $(LDFLAGS)

# Install the built plugin to the appropriate directory
install: $(OUTPUT_DIR)/$(PROJECT_NAME)
	@echo "Installing $(PROJECT_NAME).clap to ~/Library/Audio/Plug-Ins/CLAP/"
	@mkdir -p ~/Library/Audio/Plug-Ins/CLAP/
	cp -R $(BUILD_DIR)/$(PROJECT_NAME).clap ~/Library/Audio/Plug-Ins/CLAP/
