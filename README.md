# CLAP Plugin Template Generator

This repository provides a template generator for creating CLAP (CLever Audio
Plugin) plugins. It simplifies the process of setting up a new CLAP plugin
project by generating boilerplate code and project structure based on predefined
templates.

```sh
git clone --recurse-submodules https://github.com/cyrillsemenov/CLAP-plugin-template-generator.git

uv run --directory clap-plugin-generator generate
make -C test_src install

cargo -Z unstable-options -C libs/clap-validator run validate ../../test_src/build/my_plugin.clap 2>/dev/null
# /Applications/REAPER.app/Contents/MacOS/REAPER
```

```
.
├── README.md
├── clap-plugin-generator
│   ├── README.md
│   ├── pyproject.toml
│   ├── src
│   │   └── clap_plugin_generator
│   │       ├── __init__.py
│   │       ├── clap_data
│   │       │   ├── __init__.py
│   │       │   ├── clap_defs.py
│   │       │   ├── clap_enums.py
│   │       │   └── clap_extensions.py
│   │       └── clap_schema
│   │           ├── __init__.py
│   │           ├── base.py
│   │           ├── ext
│   │           │   ├── __init__.py
│   │           │   ├── audio_ports.py
│   │           │   ├── note_ports.py
│   │           │   └── params.py
│   │           └── plugin_descriptor.py
│   ├── templates
│   │   ├── clap
│   │   │   ├── Makefile.j2
│   │   │   ├── README.md.j2
│   │   │   ├── linux-plug.version.j2
│   │   │   ├── macos-symbols.txt.j2
│   │   │   ├── plugins.plist.in.j2
│   │   │   └── src
│   │   │       ├── audio_processor.c.j2
│   │   │       ├── entry.c.j2
│   │   │       ├── event_processor.c.j2
│   │   │       ├── ext
│   │   │       │   ├── audio_ports.c.j2
│   │   │       │   ├── latency.c.j2
│   │   │       │   ├── note_ports.c.j2
│   │   │       │   ├── params.c.j2
│   │   │       │   └── state.c.j2
│   │   │       ├── macos-symbols.txt.j2
│   │   │       ├── params.c.j2
│   │   │       ├── params.h.j2
│   │   │       ├── plugin.c.j2
│   │   │       └── plugin.h.j2
│   │   ├── macros.c.j2
│   │   └── plugin_main_template.c.j2
│   ├── utils
│   │   ├── Makefile
│   │   └── parse_clap_enums.c
│   └── uv.lock
├── generate.py
├── libs
│   ├── clap
│   │   ...
│   └── clap-validator
│       ...
├── sample.yaml
└── schema.json

36 directories, 180 files
```
