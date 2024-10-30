"""
This file was automatically generated from CLAP API headers
by 'CLAP Data Parser' tool

CLAP: https://github.com/free-audio/clap/
CLAP Data Parser: https://github.com/cyrillsemenov/CLAP-plugin-template-generator/utils/parse_clap_enums.c

Date: 2024-10-30 19:29
"""

from enum import StrEnum


class ClapPluginExtensions(StrEnum):
    """
    CLAP plugin extensions
    """

    UNDO = "CLAP_EXT_UNDO"
    """
    File: ../libs/clap/include/clap/ext/draft/undo.h
    
    Value: "clap.undo/4"
    """

    TRIGGERS = "CLAP_EXT_TRIGGERS"
    """
    File: ../libs/clap/include/clap/ext/draft/triggers.h
    
    Value: "clap.triggers/1"
    """

    RESOURCE_DIRECTORY = "CLAP_EXT_RESOURCE_DIRECTORY"
    """
    File: ../libs/clap/include/clap/ext/draft/resource-directory.h
    
    Value: "clap.resource-directory/1"
    """

    TUNING = "CLAP_EXT_TUNING"
    """
    File: ../libs/clap/include/clap/ext/draft/tuning.h
    
    Value: "clap.tuning/2"
    """

    PRESET_LOAD = "CLAP_EXT_PRESET_LOAD"
    """
    File: ../libs/clap/include/clap/ext/preset-load.h
    
    Value: "clap.preset-load/2"
    """

    PARAMS = "CLAP_EXT_PARAMS"
    """
    File: ../libs/clap/include/clap/ext/params.h
    
    Value: "clap.params"
    """

    NOTE_NAME = "CLAP_EXT_NOTE_NAME"
    """
    File: ../libs/clap/include/clap/ext/note-name.h
    
    Value: "clap.note-name"
    """

    REMOTE_CONTROLS = "CLAP_EXT_REMOTE_CONTROLS"
    """
    File: ../libs/clap/include/clap/ext/remote-controls.h
    
    Value: "clap.remote-controls/2"
    """

    SURROUND = "CLAP_EXT_SURROUND"
    """
    File: ../libs/clap/include/clap/ext/surround.h
    
    Value: "clap.surround/4"
    """

    AMBISONIC = "CLAP_EXT_AMBISONIC"
    """
    File: ../libs/clap/include/clap/ext/ambisonic.h
    
    Value: "clap.ambisonic/3"
    
    This extension can be used to specify the channel mapping used by the plugin.
    """

    TRACK_INFO = "CLAP_EXT_TRACK_INFO"
    """
    File: ../libs/clap/include/clap/ext/track-info.h
    
    Value: "clap.track-info/1"
    """

    NOTE_PORTS = "CLAP_EXT_NOTE_PORTS"
    """
    File: ../libs/clap/include/clap/ext/note-ports.h
    
    Value: "clap.note-ports"
    """

    AUDIO_PORTS_CONFIG = "CLAP_EXT_AUDIO_PORTS_CONFIG"
    """
    File: ../libs/clap/include/clap/ext/audio-ports-config.h
    
    Value: "clap.audio-ports-config"
    """

    VOICE_INFO = "CLAP_EXT_VOICE_INFO"
    """
    File: ../libs/clap/include/clap/ext/voice-info.h
    
    Value: "clap.voice-info"
    """

    LATENCY = "CLAP_EXT_LATENCY"
    """
    File: ../libs/clap/include/clap/ext/latency.h
    
    Value: "clap.latency"
    """

    TIMER_SUPPORT = "CLAP_EXT_TIMER_SUPPORT"
    """
    File: ../libs/clap/include/clap/ext/timer-support.h
    
    Value: "clap.timer-support"
    """

    GUI = "CLAP_EXT_GUI"
    """
    File: ../libs/clap/include/clap/ext/gui.h
    
    Value: "clap.gui"
    """

    TAIL = "CLAP_EXT_TAIL"
    """
    File: ../libs/clap/include/clap/ext/tail.h
    
    Value: "clap.tail"
    """

    CONTEXT_MENU = "CLAP_EXT_CONTEXT_MENU"
    """
    File: ../libs/clap/include/clap/ext/context-menu.h
    
    Value: "clap.context-menu/1"
    """

    POSIX_FD_SUPPORT = "CLAP_EXT_POSIX_FD_SUPPORT"
    """
    File: ../libs/clap/include/clap/ext/posix-fd-support.h
    
    Value: "clap.posix-fd-support"
    
    This extension let your plugin hook itself into the host select/poll/epoll/kqueue reactor.
    This is useful to handle asynchronous I/O on the main thread.
    """

    THREAD_POOL = "CLAP_EXT_THREAD_POOL"
    """
    File: ../libs/clap/include/clap/ext/thread-pool.h
    
    Value: "clap.thread-pool"
    """

    AUDIO_PORTS = "CLAP_EXT_AUDIO_PORTS"
    """
    File: ../libs/clap/include/clap/ext/audio-ports.h
    
    Value: "clap.audio-ports"
    """

    STATE = "CLAP_EXT_STATE"
    """
    File: ../libs/clap/include/clap/ext/state.h
    
    Value: "clap.state"
    """

    STATE_CONTEXT = "CLAP_EXT_STATE_CONTEXT"
    """
    File: ../libs/clap/include/clap/ext/state-context.h
    
    Value: "clap.state-context/2"
    """

    PARAM_INDICATION = "CLAP_EXT_PARAM_INDICATION"
    """
    File: ../libs/clap/include/clap/ext/param-indication.h
    
    Value: "clap.param-indication/4"
    """

    RENDER = "CLAP_EXT_RENDER"
    """
    File: ../libs/clap/include/clap/ext/render.h
    
    Value: "clap.render"
    """



class ClapHostExtensions(StrEnum):
    """
    CLAP host extensions
    """

    TRANSPORT_CONTROL = "CLAP_EXT_TRANSPORT_CONTROL"
    """
    File: ../libs/clap/include/clap/ext/draft/transport-control.h
    
    Value: "clap.transport-control/1"
    """

    UNDO = "CLAP_EXT_UNDO"
    """
    File: ../libs/clap/include/clap/ext/draft/undo.h
    
    Value: "clap.undo/4"
    """

    TRIGGERS = "CLAP_EXT_TRIGGERS"
    """
    File: ../libs/clap/include/clap/ext/draft/triggers.h
    
    Value: "clap.triggers/1"
    """

    RESOURCE_DIRECTORY = "CLAP_EXT_RESOURCE_DIRECTORY"
    """
    File: ../libs/clap/include/clap/ext/draft/resource-directory.h
    
    Value: "clap.resource-directory/1"
    """

    TUNING = "CLAP_EXT_TUNING"
    """
    File: ../libs/clap/include/clap/ext/draft/tuning.h
    
    Value: "clap.tuning/2"
    """

    PRESET_LOAD = "CLAP_EXT_PRESET_LOAD"
    """
    File: ../libs/clap/include/clap/ext/preset-load.h
    
    Value: "clap.preset-load/2"
    """

    PARAMS = "CLAP_EXT_PARAMS"
    """
    File: ../libs/clap/include/clap/ext/params.h
    
    Value: "clap.params"
    """

    NOTE_NAME = "CLAP_EXT_NOTE_NAME"
    """
    File: ../libs/clap/include/clap/ext/note-name.h
    
    Value: "clap.note-name"
    """

    REMOTE_CONTROLS = "CLAP_EXT_REMOTE_CONTROLS"
    """
    File: ../libs/clap/include/clap/ext/remote-controls.h
    
    Value: "clap.remote-controls/2"
    """

    SURROUND = "CLAP_EXT_SURROUND"
    """
    File: ../libs/clap/include/clap/ext/surround.h
    
    Value: "clap.surround/4"
    """

    AMBISONIC = "CLAP_EXT_AMBISONIC"
    """
    File: ../libs/clap/include/clap/ext/ambisonic.h
    
    Value: "clap.ambisonic/3"
    
    This extension can be used to specify the channel mapping used by the plugin.
    """

    TRACK_INFO = "CLAP_EXT_TRACK_INFO"
    """
    File: ../libs/clap/include/clap/ext/track-info.h
    
    Value: "clap.track-info/1"
    """

    NOTE_PORTS = "CLAP_EXT_NOTE_PORTS"
    """
    File: ../libs/clap/include/clap/ext/note-ports.h
    
    Value: "clap.note-ports"
    """

    AUDIO_PORTS_CONFIG = "CLAP_EXT_AUDIO_PORTS_CONFIG"
    """
    File: ../libs/clap/include/clap/ext/audio-ports-config.h
    
    Value: "clap.audio-ports-config"
    """

    THREAD_CHECK = "CLAP_EXT_THREAD_CHECK"
    """
    File: ../libs/clap/include/clap/ext/thread-check.h
    
    Value: "clap.thread-check"
    """

    VOICE_INFO = "CLAP_EXT_VOICE_INFO"
    """
    File: ../libs/clap/include/clap/ext/voice-info.h
    
    Value: "clap.voice-info"
    """

    LATENCY = "CLAP_EXT_LATENCY"
    """
    File: ../libs/clap/include/clap/ext/latency.h
    
    Value: "clap.latency"
    """

    EVENT_REGISTRY = "CLAP_EXT_EVENT_REGISTRY"
    """
    File: ../libs/clap/include/clap/ext/event-registry.h
    
    Value: "clap.event-registry"
    """

    TIMER_SUPPORT = "CLAP_EXT_TIMER_SUPPORT"
    """
    File: ../libs/clap/include/clap/ext/timer-support.h
    
    Value: "clap.timer-support"
    """

    GUI = "CLAP_EXT_GUI"
    """
    File: ../libs/clap/include/clap/ext/gui.h
    
    Value: "clap.gui"
    """

    TAIL = "CLAP_EXT_TAIL"
    """
    File: ../libs/clap/include/clap/ext/tail.h
    
    Value: "clap.tail"
    """

    LOG = "CLAP_EXT_LOG"
    """
    File: ../libs/clap/include/clap/ext/log.h
    
    Value: "clap.log"
    """

    CONTEXT_MENU = "CLAP_EXT_CONTEXT_MENU"
    """
    File: ../libs/clap/include/clap/ext/context-menu.h
    
    Value: "clap.context-menu/1"
    """

    POSIX_FD_SUPPORT = "CLAP_EXT_POSIX_FD_SUPPORT"
    """
    File: ../libs/clap/include/clap/ext/posix-fd-support.h
    
    Value: "clap.posix-fd-support"
    
    This extension let your plugin hook itself into the host select/poll/epoll/kqueue reactor.
    This is useful to handle asynchronous I/O on the main thread.
    """

    THREAD_POOL = "CLAP_EXT_THREAD_POOL"
    """
    File: ../libs/clap/include/clap/ext/thread-pool.h
    
    Value: "clap.thread-pool"
    """

    AUDIO_PORTS = "CLAP_EXT_AUDIO_PORTS"
    """
    File: ../libs/clap/include/clap/ext/audio-ports.h
    
    Value: "clap.audio-ports"
    """

    STATE = "CLAP_EXT_STATE"
    """
    File: ../libs/clap/include/clap/ext/state.h
    
    Value: "clap.state"
    """


