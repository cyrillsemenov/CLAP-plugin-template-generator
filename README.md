# CLAP Plugin Template Generator

This repository provides a template generator for creating CLAP (CLever Audio
Plugin) plugins. It simplifies the process of setting up a new CLAP plugin
project by generating boilerplate code and project structure based on predefined
templates.

```sh
git clone --recurse-submodules https://github.com/cyrillsemenov/CLAP-plugin-template-generator.git

uv run cli render my_plugin
make -C my_plugin install
clap-validator validate my_plugin/build/my_plugin.clap 2>/dev/null
# /Applications/REAPER.app/Contents/MacOS/REAPER
```
