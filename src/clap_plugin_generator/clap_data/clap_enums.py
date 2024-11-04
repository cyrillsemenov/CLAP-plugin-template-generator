"""
This file was automatically generated from CLAP API headers
by 'CLAP Data Parser' tool

CLAP: https://github.com/free-audio/clap/
CLAP Data Parser: https://github.com/cyrillsemenov/CLAP-plugin-template-generator/utils/parse_clap_enums.c

Date: 2024-11-02 15:51
"""

from enum import StrEnum


class ClapTriggerIsAutomatablePer(StrEnum):
    """
    File: ../libs/clap/include/clap/ext/draft/triggers.h
    """

    NOTE_ID = "CLAP_TRIGGER_IS_AUTOMATABLE_PER_NOTE_ID"
    """
    Does this trigger support per note automations?
    """

    KEY = "CLAP_TRIGGER_IS_AUTOMATABLE_PER_KEY"
    """
    Does this trigger support per key automations?
    """

    CHANNEL = "CLAP_TRIGGER_IS_AUTOMATABLE_PER_CHANNEL"
    """
    Does this trigger support per channel automations?
    """

    PORT = "CLAP_TRIGGER_IS_AUTOMATABLE_PER_PORT"
    """
    Does this trigger support per port automations?
    """



class ClapTriggerRescan(StrEnum):
    """
    File: ../libs/clap/include/clap/ext/draft/triggers.h
    """

    INFO = "CLAP_TRIGGER_RESCAN_INFO"
    """
    The trigger info did change, use this flag for:
    - name change
    - module change
    New info takes effect immediately.
    """

    ALL = "CLAP_TRIGGER_RESCAN_ALL"
    """
    Invalidates everything the host knows about triggers.
    It can only be used while the plugin is deactivated.
    If the plugin is activated use clap_host->restart() and delay any change until the host calls
    clap_plugin->deactivate().
    
    You must use this flag if:
    - some triggers were added or removed.
    - some triggers had critical changes:
      - is_per_note (flag)
      - is_per_key (flag)
      - is_per_channel (flag)
      - is_per_port (flag)
      - cookie
    """



class ClapTriggerClear(StrEnum):
    """
    File: ../libs/clap/include/clap/ext/draft/triggers.h
    """

    ALL = "CLAP_TRIGGER_CLEAR_ALL"
    """
    Clears all possible references to a trigger
    """

    AUTOMATIONS = "CLAP_TRIGGER_CLEAR_AUTOMATIONS"
    """
    Clears all automations to a trigger
    """



class ClapParam(StrEnum):
    """
    File: ../libs/clap/include/clap/ext/params.h
    """

    IS_STEPPED = "CLAP_PARAM_IS_STEPPED"
    """
    Is this param stepped? (integer values only)
    if so the double value is converted to integer using a cast (equivalent to trunc).
    """

    IS_PERIODIC = "CLAP_PARAM_IS_PERIODIC"
    """
    Useful for periodic parameters like a phase
    """

    IS_HIDDEN = "CLAP_PARAM_IS_HIDDEN"
    """
    The parameter should not be shown to the user, because it is currently not used.
    It is not necessary to process automation for this parameter.
    """

    IS_READONLY = "CLAP_PARAM_IS_READONLY"
    """
    The parameter can't be changed by the host.
    """

    IS_BYPASS = "CLAP_PARAM_IS_BYPASS"
    """
    This parameter is used to merge the plugin and host bypass button.
    It implies that the parameter is stepped.
    min: 0 -> bypass off
    max: 1 -> bypass on
    """

    IS_AUTOMATABLE = "CLAP_PARAM_IS_AUTOMATABLE"
    """
    When set:
    - automation can be recorded
    - automation can be played back
    
    The host can send live user changes for this parameter regardless of this flag.
    
    If this parameter affects the internal processing structure of the plugin, ie: max delay, fft
    size, ... and the plugins needs to re-allocate its working buffers, then it should call
    host->request_restart(), and perform the change once the plugin is re-activated.
    """

    IS_AUTOMATABLE_PER_NOTE_ID = "CLAP_PARAM_IS_AUTOMATABLE_PER_NOTE_ID"
    """
    Does this parameter support per note automations?
    """

    IS_AUTOMATABLE_PER_KEY = "CLAP_PARAM_IS_AUTOMATABLE_PER_KEY"
    """
    Does this parameter support per key automations?
    """

    IS_AUTOMATABLE_PER_CHANNEL = "CLAP_PARAM_IS_AUTOMATABLE_PER_CHANNEL"
    """
    Does this parameter support per channel automations?
    """

    IS_AUTOMATABLE_PER_PORT = "CLAP_PARAM_IS_AUTOMATABLE_PER_PORT"
    """
    Does this parameter support per port automations?
    """

    IS_MODULATABLE = "CLAP_PARAM_IS_MODULATABLE"
    """
    Does this parameter support the modulation signal?
    """

    IS_MODULATABLE_PER_NOTE_ID = "CLAP_PARAM_IS_MODULATABLE_PER_NOTE_ID"
    """
    Does this parameter support per note modulations?
    """

    IS_MODULATABLE_PER_KEY = "CLAP_PARAM_IS_MODULATABLE_PER_KEY"
    """
    Does this parameter support per key modulations?
    """

    IS_MODULATABLE_PER_CHANNEL = "CLAP_PARAM_IS_MODULATABLE_PER_CHANNEL"
    """
    Does this parameter support per channel modulations?
    """

    IS_MODULATABLE_PER_PORT = "CLAP_PARAM_IS_MODULATABLE_PER_PORT"
    """
    Does this parameter support per port modulations?
    """

    REQUIRES_PROCESS = "CLAP_PARAM_REQUIRES_PROCESS"
    """
    Any change to this parameter will affect the plugin output and requires to be done via
    process() if the plugin is active.
    
    A simple example would be a DC Offset, changing it will change the output signal and must be
    processed.
    """

    IS_ENUM = "CLAP_PARAM_IS_ENUM"
    """
    This parameter represents an enumerated value.
    If you set this flag, then you must set CLAP_PARAM_IS_STEPPED too.
    All values from min to max must not have a blank value_to_text().
    """



class ClapParamRescan(StrEnum):
    """
    File: ../libs/clap/include/clap/ext/params.h
    """

    VALUES = "CLAP_PARAM_RESCAN_VALUES"
    """
    The parameter values did change, eg. after loading a preset.
    The host will scan all the parameters value.
    The host will not record those changes as automation points.
    New values takes effect immediately.
    """

    TEXT = "CLAP_PARAM_RESCAN_TEXT"
    """
    The value to text conversion changed, and the text needs to be rendered again.
    """

    INFO = "CLAP_PARAM_RESCAN_INFO"
    """
    The parameter info did change, use this flag for:
    - name change
    - module change
    - is_periodic (flag)
    - is_hidden (flag)
    New info takes effect immediately.
    """

    ALL = "CLAP_PARAM_RESCAN_ALL"
    """
    Invalidates everything the host knows about parameters.
    It can only be used while the plugin is deactivated.
    If the plugin is activated use clap_host->restart() and delay any change until the host calls
    clap_plugin->deactivate().
    
    You must use this flag if:
    - some parameters were added or removed.
    - some parameters had critical changes:
      - is_per_note (flag)
      - is_per_key (flag)
      - is_per_channel (flag)
      - is_per_port (flag)
      - is_readonly (flag)
      - is_bypass (flag)
      - is_stepped (flag)
      - is_modulatable (flag)
      - min_value
      - max_value
      - cookie
    """



class ClapParamClear(StrEnum):
    """
    File: ../libs/clap/include/clap/ext/params.h
    """

    ALL = "CLAP_PARAM_CLEAR_ALL"
    """
    Clears all possible references to a parameter
    """

    AUTOMATIONS = "CLAP_PARAM_CLEAR_AUTOMATIONS"
    """
    Clears all automations to a parameter
    """

    MODULATIONS = "CLAP_PARAM_CLEAR_MODULATIONS"
    """
    Clears all modulations to a parameter
    """



class ClapSurround(StrEnum):
    """
    File: ../libs/clap/include/clap/ext/surround.h
    """

    FL = "CLAP_SURROUND_FL"
    """
    Front Left
    """

    FR = "CLAP_SURROUND_FR"
    """
    Front Right
    """

    FC = "CLAP_SURROUND_FC"
    """
    Front Center
    """

    LFE = "CLAP_SURROUND_LFE"
    """
    Low Frequency
    """

    BL = "CLAP_SURROUND_BL"
    """
    Back Left
    """

    BR = "CLAP_SURROUND_BR"
    """
    Back Right
    """

    FLC = "CLAP_SURROUND_FLC"
    """
    Front Left of Center
    """

    FRC = "CLAP_SURROUND_FRC"
    """
    Front Right of Center
    """

    BC = "CLAP_SURROUND_BC"
    """
    Back Center
    """

    SL = "CLAP_SURROUND_SL"
    """
    Side Left
    """

    SR = "CLAP_SURROUND_SR"
    """
    Side Right
    """

    TC = "CLAP_SURROUND_TC"
    """
    Top Center
    """

    TFL = "CLAP_SURROUND_TFL"
    """
    Front Left Height
    """

    TFC = "CLAP_SURROUND_TFC"
    """
    Front Center Height
    """

    TFR = "CLAP_SURROUND_TFR"
    """
    Front Right Height
    """

    TBL = "CLAP_SURROUND_TBL"
    """
    Rear Left Height
    """

    TBC = "CLAP_SURROUND_TBC"
    """
    Rear Center Height
    """

    TBR = "CLAP_SURROUND_TBR"
    """
    Rear Right Height
    """



class ClapAmbisonicOrdering(StrEnum):
    """
    File: ../libs/clap/include/clap/ext/ambisonic.h
    """

    FUMA = "CLAP_AMBISONIC_ORDERING_FUMA"
    """
    FuMa channel ordering
    """

    ACN = "CLAP_AMBISONIC_ORDERING_ACN"
    """
    ACN channel ordering
    """



class ClapAmbisonicNormalization(StrEnum):
    """
    File: ../libs/clap/include/clap/ext/ambisonic.h
    """

    MAXN = "CLAP_AMBISONIC_NORMALIZATION_MAXN"
    SN3D = "CLAP_AMBISONIC_NORMALIZATION_SN3D"
    N3D = "CLAP_AMBISONIC_NORMALIZATION_N3D"
    SN2D = "CLAP_AMBISONIC_NORMALIZATION_SN2D"
    N2D = "CLAP_AMBISONIC_NORMALIZATION_N2D"


class ClapTrackInfo(StrEnum):
    """
    File: ../libs/clap/include/clap/ext/track-info.h
    """

    HAS_TRACK_NAME = "CLAP_TRACK_INFO_HAS_TRACK_NAME"
    HAS_TRACK_COLOR = "CLAP_TRACK_INFO_HAS_TRACK_COLOR"
    HAS_AUDIO_CHANNEL = "CLAP_TRACK_INFO_HAS_AUDIO_CHANNEL"
    IS_FOR_RETURN_TRACK = "CLAP_TRACK_INFO_IS_FOR_RETURN_TRACK"
    """
    This plugin is on a return track, initialize with wet 100%
    """

    IS_FOR_BUS = "CLAP_TRACK_INFO_IS_FOR_BUS"
    """
    This plugin is on a bus track, initialize with appropriate settings for bus processing
    """

    IS_FOR_MASTER = "CLAP_TRACK_INFO_IS_FOR_MASTER"
    """
    This plugin is on the master, initialize with appropriate settings for channel processing
    """



class ClapNoteDialect(StrEnum):
    """
    File: ../libs/clap/include/clap/ext/note-ports.h
    """

    CLAP = "CLAP_NOTE_DIALECT_CLAP"
    """
    Uses clap_event_note and clap_event_note_expression.
    """

    MIDI = "CLAP_NOTE_DIALECT_MIDI"
    """
    Uses clap_event_midi, no polyphonic expression
    """

    MIDI_MPE = "CLAP_NOTE_DIALECT_MIDI_MPE"
    """
    Uses clap_event_midi, with polyphonic expression (MPE)
    """

    MIDI2 = "CLAP_NOTE_DIALECT_MIDI2"
    """
    Uses clap_event_midi2
    """



class ClapNotePortsRescan(StrEnum):
    """
    File: ../libs/clap/include/clap/ext/note-ports.h
    """

    ALL = "CLAP_NOTE_PORTS_RESCAN_ALL"
    """
    The ports have changed, the host shall perform a full scan of the ports.
    This flag can only be used if the plugin is not active.
    If the plugin active, call host->request_restart() and then call rescan()
    when the host calls deactivate()
    """

    NAMES = "CLAP_NOTE_PORTS_RESCAN_NAMES"
    """
    The ports name did change, the host can scan them right away.
    """



class ClapLog(StrEnum):
    """
    File: ../libs/clap/include/clap/ext/log.h
    """

    DEBUG = "CLAP_LOG_DEBUG"
    INFO = "CLAP_LOG_INFO"
    WARNING = "CLAP_LOG_WARNING"
    ERROR = "CLAP_LOG_ERROR"
    FATAL = "CLAP_LOG_FATAL"
    HOST_MISBEHAVING = "CLAP_LOG_HOST_MISBEHAVING"
    """
    These severities should be used to report misbehaviour.
    The plugin one can be used by a layer between the plugin and the host.
    """

    PLUGIN_MISBEHAVING = "CLAP_LOG_PLUGIN_MISBEHAVING"
    """
    These severities should be used to report misbehaviour.
    The plugin one can be used by a layer between the plugin and the host.
    """



class ClapContextMenuTargetKind(StrEnum):
    """
    File: ../libs/clap/include/clap/ext/context-menu.h
    
    There can be different target kind for a context menu
    """

    GLOBAL = "CLAP_CONTEXT_MENU_TARGET_KIND_GLOBAL"
    PARAM = "CLAP_CONTEXT_MENU_TARGET_KIND_PARAM"


class ClapContextMenuItem(StrEnum):
    """
    File: ../libs/clap/include/clap/ext/context-menu.h
    """

    ENTRY = "CLAP_CONTEXT_MENU_ITEM_ENTRY"
    """
    Adds a clickable menu entry.
    data: const clap_context_menu_item_entry_t*
    """

    CHECK_ENTRY = "CLAP_CONTEXT_MENU_ITEM_CHECK_ENTRY"
    """
    Adds a clickable menu entry which will feature both a checkmark and a label.
    data: const clap_context_menu_item_check_entry_t*
    """

    SEPARATOR = "CLAP_CONTEXT_MENU_ITEM_SEPARATOR"
    """
    Adds a separator line.
    data: NULL
    """

    BEGIN_SUBMENU = "CLAP_CONTEXT_MENU_ITEM_BEGIN_SUBMENU"
    """
    Starts a sub menu with the given label.
    data: const clap_context_menu_item_begin_submenu_t*
    """

    END_SUBMENU = "CLAP_CONTEXT_MENU_ITEM_END_SUBMENU"
    """
    Ends the current sub menu.
    data: NULL
    """

    TITLE = "CLAP_CONTEXT_MENU_ITEM_TITLE"
    """
    Adds a title entry
    data: const clap_context_menu_item_title_t *
    """



class ClapPosixFd(StrEnum):
    """
    File: ../libs/clap/include/clap/ext/posix-fd-support.h
    """

    READ = "CLAP_POSIX_FD_READ"
    """
    IO events flags, they can be used to form a mask which describes:
    - which events you are interested in (register_fd/modify_fd)
    - which events happened (on_fd)
    """

    WRITE = "CLAP_POSIX_FD_WRITE"
    """
    IO events flags, they can be used to form a mask which describes:
    - which events you are interested in (register_fd/modify_fd)
    - which events happened (on_fd)
    """

    ERROR = "CLAP_POSIX_FD_ERROR"
    """
    IO events flags, they can be used to form a mask which describes:
    - which events you are interested in (register_fd/modify_fd)
    - which events happened (on_fd)
    """



class ClapAudioPort(StrEnum):
    """
    File: ../libs/clap/include/clap/ext/audio-ports.h
    """

    IS_MAIN = "CLAP_AUDIO_PORT_IS_MAIN"
    """
    This port is the main audio input or output.
    There can be only one main input and main output.
    Main port must be at index 0.
    """

    SUPPORTS_64BITS = "CLAP_AUDIO_PORT_SUPPORTS_64BITS"
    """
    This port can be used with 64 bits audio
    """

    PREFERS_64BITS = "CLAP_AUDIO_PORT_PREFERS_64BITS"
    """
    64 bits audio is preferred with this port
    """

    REQUIRES_COMMON_SAMPLE_SIZE = "CLAP_AUDIO_PORT_REQUIRES_COMMON_SAMPLE_SIZE"
    """
    This port must be used with the same sample size as all the other ports which have this flag.
    In other words if all ports have this flag then the plugin may either be used entirely with
    64 bits audio or 32 bits audio, but it can't be mixed.
    """



class ClapAudioPortsRescan(StrEnum):
    """
    File: ../libs/clap/include/clap/ext/audio-ports.h
    """

    NAMES = "CLAP_AUDIO_PORTS_RESCAN_NAMES"
    """
    The ports name did change, the host can scan them right away.
    """

    FLAGS = "CLAP_AUDIO_PORTS_RESCAN_FLAGS"
    """
    [!active] The flags did change
    """

    CHANNEL_COUNT = "CLAP_AUDIO_PORTS_RESCAN_CHANNEL_COUNT"
    """
    [!active] The channel_count did change
    """

    PORT_TYPE = "CLAP_AUDIO_PORTS_RESCAN_PORT_TYPE"
    """
    [!active] The port type did change
    """

    IN_PLACE_PAIR = "CLAP_AUDIO_PORTS_RESCAN_IN_PLACE_PAIR"
    """
    [!active] The in-place pair did change, this requires.
    """

    LIST = "CLAP_AUDIO_PORTS_RESCAN_LIST"
    """
    [!active] The list of ports have changed: entries have been removed/added.
    """



class ClapPluginStateContextType(StrEnum):
    """
    File: ../libs/clap/include/clap/ext/state-context.h
    """

    PRESET = "CLAP_STATE_CONTEXT_FOR_PRESET"
    """
    suitable for storing and loading a state as a preset
    """

    DUPLICATE = "CLAP_STATE_CONTEXT_FOR_DUPLICATE"
    """
    suitable for duplicating a plugin instance
    """

    PROJECT = "CLAP_STATE_CONTEXT_FOR_PROJECT"
    """
    suitable for storing and loading a state within a project/song
    """



class ClapParamIndicationAutomation(StrEnum):
    """
    File: ../libs/clap/include/clap/ext/param-indication.h
    """

    NONE = "CLAP_PARAM_INDICATION_AUTOMATION_NONE"
    """
    The host doesn't have an automation for this parameter
    """

    PRESENT = "CLAP_PARAM_INDICATION_AUTOMATION_PRESENT"
    """
    The host has an automation for this parameter, but it isn't playing it
    """

    PLAYING = "CLAP_PARAM_INDICATION_AUTOMATION_PLAYING"
    """
    The host is playing an automation for this parameter
    """

    RECORDING = "CLAP_PARAM_INDICATION_AUTOMATION_RECORDING"
    """
    The host is recording an automation on this parameter
    """

    OVERRIDING = "CLAP_PARAM_INDICATION_AUTOMATION_OVERRIDING"
    """
    The host should play an automation for this parameter, but the user has started to adjust this
    parameter and is overriding the automation playback
    """



class ClapRender(StrEnum):
    """
    File: ../libs/clap/include/clap/ext/render.h
    """

    REALTIME = "CLAP_RENDER_REALTIME"
    """
    Default setting, for "realtime" processing
    """

    OFFLINE = "CLAP_RENDER_OFFLINE"
    """
    For processing without realtime pressure
    The plugin may use more expensive algorithms for higher sound quality.
    """



class ClapEventFlags(StrEnum):
    """
    File: ../libs/clap/include/clap/events.h
    """

    IS_LIVE = "CLAP_EVENT_IS_LIVE"
    """
    Indicate a live user event, for example a user turning a physical knob
    or playing a physical key.
    """

    DONT_RECORD = "CLAP_EVENT_DONT_RECORD"
    """
    Indicate that the event should not be recorded.
    For example this is useful when a parameter changes because of a MIDI CC,
    because if the host records both the MIDI CC automation and the parameter
    automation there will be a conflict.
    """



class ClapEvent(StrEnum):
    """
    File: ../libs/clap/include/clap/events.h
    
    Some of the following events overlap, a note on can be expressed with:
    - CLAP_EVENT_NOTE_ON
    - CLAP_EVENT_MIDI
    - CLAP_EVENT_MIDI2
    
    The preferred way of sending a note event is to use CLAP_EVENT_NOTE_*.
    
    The same event must not be sent twice: it is forbidden to send a the same note on
    encoded with both CLAP_EVENT_NOTE_ON and CLAP_EVENT_MIDI.
    
    The plugins are encouraged to be able to handle note events encoded as raw midi or midi2,
    or implement clap_plugin_event_filter and reject raw midi and midi2 events.
    """

    NOTE_ON = "CLAP_EVENT_NOTE_ON"
    """
    NOTE_ON and NOTE_OFF represent a key pressed and key released event, respectively.
    A NOTE_ON with a velocity of 0 is valid and should not be interpreted as a NOTE_OFF.
    
    NOTE_CHOKE is meant to choke the voice(s), like in a drum machine when a closed hihat
    chokes an open hihat. This event can be sent by the host to the plugin. Here are two use
    cases:
    - a plugin is inside a drum pad in Bitwig Studio's drum machine, and this pad is choked by
      another one
    - the user double-clicks the DAW's stop button in the transport which then stops the sound on
      every track
    
    NOTE_END is sent by the plugin to the host. The port, channel, key and note_id are those given
    by the host in the NOTE_ON event. In other words, this event is matched against the
    plugin's note input port.
    NOTE_END is useful to help the host to match the plugin's voice life time.
    
    When using polyphonic modulations, the host has to allocate and release voices for its
    polyphonic modulator. Yet only the plugin effectively knows when the host should terminate
    a voice. NOTE_END solves that issue in a non-intrusive and cooperative way.
    
    CLAP assumes that the host will allocate a unique voice on NOTE_ON event for a given port,
    channel and key. This voice will run until the plugin will instruct the host to terminate
    it by sending a NOTE_END event.
    
    Consider the following sequence:
    - process()
       Host->Plugin NoteOn(port:0, channel:0, key:16, time:t0)
       Host->Plugin NoteOn(port:0, channel:0, key:64, time:t0)
       Host->Plugin NoteOff(port:0, channel:0, key:16, t1)
       Host->Plugin NoteOff(port:0, channel:0, key:64, t1)
       # on t2, both notes did terminate
       Host->Plugin NoteOn(port:0, channel:0, key:64, t3)
       # Here the plugin finished processing all the frames and will tell the host
       # to terminate the voice on key 16 but not 64, because a note has been started at t3
       Plugin->Host NoteEnd(port:0, channel:0, key:16, time:ignored)
    
    These four events use clap_event_note.
    """

    NOTE_OFF = "CLAP_EVENT_NOTE_OFF"
    """
    NOTE_ON and NOTE_OFF represent a key pressed and key released event, respectively.
    A NOTE_ON with a velocity of 0 is valid and should not be interpreted as a NOTE_OFF.
    
    NOTE_CHOKE is meant to choke the voice(s), like in a drum machine when a closed hihat
    chokes an open hihat. This event can be sent by the host to the plugin. Here are two use
    cases:
    - a plugin is inside a drum pad in Bitwig Studio's drum machine, and this pad is choked by
      another one
    - the user double-clicks the DAW's stop button in the transport which then stops the sound on
      every track
    
    NOTE_END is sent by the plugin to the host. The port, channel, key and note_id are those given
    by the host in the NOTE_ON event. In other words, this event is matched against the
    plugin's note input port.
    NOTE_END is useful to help the host to match the plugin's voice life time.
    
    When using polyphonic modulations, the host has to allocate and release voices for its
    polyphonic modulator. Yet only the plugin effectively knows when the host should terminate
    a voice. NOTE_END solves that issue in a non-intrusive and cooperative way.
    
    CLAP assumes that the host will allocate a unique voice on NOTE_ON event for a given port,
    channel and key. This voice will run until the plugin will instruct the host to terminate
    it by sending a NOTE_END event.
    
    Consider the following sequence:
    - process()
       Host->Plugin NoteOn(port:0, channel:0, key:16, time:t0)
       Host->Plugin NoteOn(port:0, channel:0, key:64, time:t0)
       Host->Plugin NoteOff(port:0, channel:0, key:16, t1)
       Host->Plugin NoteOff(port:0, channel:0, key:64, t1)
       # on t2, both notes did terminate
       Host->Plugin NoteOn(port:0, channel:0, key:64, t3)
       # Here the plugin finished processing all the frames and will tell the host
       # to terminate the voice on key 16 but not 64, because a note has been started at t3
       Plugin->Host NoteEnd(port:0, channel:0, key:16, time:ignored)
    
    These four events use clap_event_note.
    """

    NOTE_CHOKE = "CLAP_EVENT_NOTE_CHOKE"
    """
    NOTE_ON and NOTE_OFF represent a key pressed and key released event, respectively.
    A NOTE_ON with a velocity of 0 is valid and should not be interpreted as a NOTE_OFF.
    
    NOTE_CHOKE is meant to choke the voice(s), like in a drum machine when a closed hihat
    chokes an open hihat. This event can be sent by the host to the plugin. Here are two use
    cases:
    - a plugin is inside a drum pad in Bitwig Studio's drum machine, and this pad is choked by
      another one
    - the user double-clicks the DAW's stop button in the transport which then stops the sound on
      every track
    
    NOTE_END is sent by the plugin to the host. The port, channel, key and note_id are those given
    by the host in the NOTE_ON event. In other words, this event is matched against the
    plugin's note input port.
    NOTE_END is useful to help the host to match the plugin's voice life time.
    
    When using polyphonic modulations, the host has to allocate and release voices for its
    polyphonic modulator. Yet only the plugin effectively knows when the host should terminate
    a voice. NOTE_END solves that issue in a non-intrusive and cooperative way.
    
    CLAP assumes that the host will allocate a unique voice on NOTE_ON event for a given port,
    channel and key. This voice will run until the plugin will instruct the host to terminate
    it by sending a NOTE_END event.
    
    Consider the following sequence:
    - process()
       Host->Plugin NoteOn(port:0, channel:0, key:16, time:t0)
       Host->Plugin NoteOn(port:0, channel:0, key:64, time:t0)
       Host->Plugin NoteOff(port:0, channel:0, key:16, t1)
       Host->Plugin NoteOff(port:0, channel:0, key:64, t1)
       # on t2, both notes did terminate
       Host->Plugin NoteOn(port:0, channel:0, key:64, t3)
       # Here the plugin finished processing all the frames and will tell the host
       # to terminate the voice on key 16 but not 64, because a note has been started at t3
       Plugin->Host NoteEnd(port:0, channel:0, key:16, time:ignored)
    
    These four events use clap_event_note.
    """

    NOTE_END = "CLAP_EVENT_NOTE_END"
    """
    NOTE_ON and NOTE_OFF represent a key pressed and key released event, respectively.
    A NOTE_ON with a velocity of 0 is valid and should not be interpreted as a NOTE_OFF.
    
    NOTE_CHOKE is meant to choke the voice(s), like in a drum machine when a closed hihat
    chokes an open hihat. This event can be sent by the host to the plugin. Here are two use
    cases:
    - a plugin is inside a drum pad in Bitwig Studio's drum machine, and this pad is choked by
      another one
    - the user double-clicks the DAW's stop button in the transport which then stops the sound on
      every track
    
    NOTE_END is sent by the plugin to the host. The port, channel, key and note_id are those given
    by the host in the NOTE_ON event. In other words, this event is matched against the
    plugin's note input port.
    NOTE_END is useful to help the host to match the plugin's voice life time.
    
    When using polyphonic modulations, the host has to allocate and release voices for its
    polyphonic modulator. Yet only the plugin effectively knows when the host should terminate
    a voice. NOTE_END solves that issue in a non-intrusive and cooperative way.
    
    CLAP assumes that the host will allocate a unique voice on NOTE_ON event for a given port,
    channel and key. This voice will run until the plugin will instruct the host to terminate
    it by sending a NOTE_END event.
    
    Consider the following sequence:
    - process()
       Host->Plugin NoteOn(port:0, channel:0, key:16, time:t0)
       Host->Plugin NoteOn(port:0, channel:0, key:64, time:t0)
       Host->Plugin NoteOff(port:0, channel:0, key:16, t1)
       Host->Plugin NoteOff(port:0, channel:0, key:64, t1)
       # on t2, both notes did terminate
       Host->Plugin NoteOn(port:0, channel:0, key:64, t3)
       # Here the plugin finished processing all the frames and will tell the host
       # to terminate the voice on key 16 but not 64, because a note has been started at t3
       Plugin->Host NoteEnd(port:0, channel:0, key:16, time:ignored)
    
    These four events use clap_event_note.
    """

    NOTE_EXPRESSION = "CLAP_EVENT_NOTE_EXPRESSION"
    """
    Represents a note expression.
    Uses clap_event_note_expression.
    """

    PARAM_VALUE = "CLAP_EVENT_PARAM_VALUE"
    """
    PARAM_VALUE sets the parameter's value; uses clap_event_param_value.
    PARAM_MOD sets the parameter's modulation amount; uses clap_event_param_mod.
    
    The value heard is: param_value + param_mod.
    
    In case of a concurrent global value/modulation versus a polyphonic one,
    the voice should only use the polyphonic one and the polyphonic modulation
    amount will already include the monophonic signal.
    """

    PARAM_MOD = "CLAP_EVENT_PARAM_MOD"
    """
    PARAM_VALUE sets the parameter's value; uses clap_event_param_value.
    PARAM_MOD sets the parameter's modulation amount; uses clap_event_param_mod.
    
    The value heard is: param_value + param_mod.
    
    In case of a concurrent global value/modulation versus a polyphonic one,
    the voice should only use the polyphonic one and the polyphonic modulation
    amount will already include the monophonic signal.
    """

    PARAM_GESTURE_BEGIN = "CLAP_EVENT_PARAM_GESTURE_BEGIN"
    """
    Indicates that the user started or finished adjusting a knob.
    This is not mandatory to wrap parameter changes with gesture events, but this improves
    the user experience a lot when recording automation or overriding automation playback.
    Uses clap_event_param_gesture.
    """

    PARAM_GESTURE_END = "CLAP_EVENT_PARAM_GESTURE_END"
    """
    Indicates that the user started or finished adjusting a knob.
    This is not mandatory to wrap parameter changes with gesture events, but this improves
    the user experience a lot when recording automation or overriding automation playback.
    Uses clap_event_param_gesture.
    """

    TRANSPORT = "CLAP_EVENT_TRANSPORT"
    """
    update the transport info; clap_event_transport
    """

    MIDI = "CLAP_EVENT_MIDI"
    """
    raw midi event; clap_event_midi
    """

    MIDI_SYSEX = "CLAP_EVENT_MIDI_SYSEX"
    """
    raw midi sysex event; clap_event_midi_sysex
    """

    MIDI2 = "CLAP_EVENT_MIDI2"
    """
    raw midi 2 event; clap_event_midi2
    """



class ClapNoteExpression(StrEnum):
    """
    File: ../libs/clap/include/clap/events.h
    
    Note Expressions are well named modifications of a voice targeted to
    voices using the same wildcard rules described above. Note Expressions are delivered
    as sample accurate events and should be applied at the sample when received.
    
    Note expressions are a statement of value, not cumulative. A PAN event of 0 followed by 1
    followed by 0.5 would pan hard left, hard right, and center. They are intended as
    an offset from the non-note-expression voice default. A voice which had a volume of
    -20db absent note expressions which received a +4db note expression would move the
    voice to -16db.
    
    A plugin which receives a note expression at the same sample as a NOTE_ON event
    should apply that expression to all generated samples. A plugin which receives
    a note expression after a NOTE_ON event should initiate the voice with default
    values and then apply the note expression when received. A plugin may make a choice
    to smooth note expression streams.
    """

    VOLUME = "CLAP_NOTE_EXPRESSION_VOLUME"
    """
    with 0 < x <= 4, plain = 20 * log(x)
    """

    PAN = "CLAP_NOTE_EXPRESSION_PAN"
    """
    pan, 0 left, 0.5 center, 1 right
    """

    TUNING = "CLAP_NOTE_EXPRESSION_TUNING"
    """
    Relative tuning in semitones, from -120 to +120. Semitones are in
    equal temperament and are doubles; the resulting note would be
    retuned by `100 * evt->value` cents.
    """

    VIBRATO = "CLAP_NOTE_EXPRESSION_VIBRATO"
    """
    0..1
    """

    EXPRESSION = "CLAP_NOTE_EXPRESSION_EXPRESSION"
    """
    0..1
    """

    BRIGHTNESS = "CLAP_NOTE_EXPRESSION_BRIGHTNESS"
    """
    0..1
    """

    PRESSURE = "CLAP_NOTE_EXPRESSION_PRESSURE"
    """
    0..1
    """



class ClapTransportFlags(StrEnum):
    """
    File: ../libs/clap/include/clap/events.h
    """

    HAS_TEMPO = "CLAP_TRANSPORT_HAS_TEMPO"
    HAS_BEATS_TIMELINE = "CLAP_TRANSPORT_HAS_BEATS_TIMELINE"
    HAS_SECONDS_TIMELINE = "CLAP_TRANSPORT_HAS_SECONDS_TIMELINE"
    HAS_TIME_SIGNATURE = "CLAP_TRANSPORT_HAS_TIME_SIGNATURE"
    IS_PLAYING = "CLAP_TRANSPORT_IS_PLAYING"
    IS_RECORDING = "CLAP_TRANSPORT_IS_RECORDING"
    IS_LOOP_ACTIVE = "CLAP_TRANSPORT_IS_LOOP_ACTIVE"
    IS_WITHIN_PRE_ROLL = "CLAP_TRANSPORT_IS_WITHIN_PRE_ROLL"


class Clap(StrEnum):
    """
    File: ../libs/clap/include/clap/string-sizes.h
    """

    NAME_SIZE = "CLAP_NAME_SIZE"
    """
    String capacity for names that can be displayed to the user.
    """

    PATH_SIZE = "CLAP_PATH_SIZE"
    """
    String capacity for describing a path, like a parameter in a module hierarchy or path within a
    set of nested track groups.
    
    This is not suited for describing a file path on the disk, as NTFS allows up to 32K long
    paths.
    """



class ClapProcess(StrEnum):
    """
    File: ../libs/clap/include/clap/process.h
    """

    ERROR = "CLAP_PROCESS_ERROR"
    """
    Processing failed. The output buffer must be discarded.
    """

    CONTINUE = "CLAP_PROCESS_CONTINUE"
    """
    Processing succeeded, keep processing.
    """

    CONTINUE_IF_NOT_QUIET = "CLAP_PROCESS_CONTINUE_IF_NOT_QUIET"
    """
    Processing succeeded, keep processing if the output is not quiet.
    """

    TAIL = "CLAP_PROCESS_TAIL"
    """
    Rely upon the plugin's tail to determine if the plugin should continue to process.
    see clap_plugin_tail
    """

    SLEEP = "CLAP_PROCESS_SLEEP"
    """
    Processing succeeded, but no more processing is required,
    until the next event or variation in audio input.
    """



class ClapPresetDiscoveryLocationKind(StrEnum):
    """
    File: ../libs/clap/include/clap/factory/preset-discovery.h
    """

    FILE = "CLAP_PRESET_DISCOVERY_LOCATION_FILE"
    """
    The preset are located in a file on the OS filesystem.
    The location is then a path which works with the OS file system functions (open, stat, ...)
    So both '/' and '\' shall work on Windows as a separator.
    """

    PLUGIN = "CLAP_PRESET_DISCOVERY_LOCATION_PLUGIN"
    """
    The preset is bundled within the plugin DSO itself.
    The location must then be null, as the preset are within the plugin itself and then the plugin
    will act as a preset container.
    """



class ClapPresetDiscoveryFlags(StrEnum):
    """
    File: ../libs/clap/include/clap/factory/preset-discovery.h
    """

    FACTORY_CONTENT = "CLAP_PRESET_DISCOVERY_IS_FACTORY_CONTENT"
    """
    This is for factory or sound-pack presets.
    """

    USER_CONTENT = "CLAP_PRESET_DISCOVERY_IS_USER_CONTENT"
    """
    This is for user presets.
    """

    DEMO_CONTENT = "CLAP_PRESET_DISCOVERY_IS_DEMO_CONTENT"
    """
    This location is meant for demo presets, those are preset which may trigger
    some limitation in the plugin because they require additional features which the user
    needs to purchase or the content itself needs to be bought and is only available in
    demo mode.
    """

    FAVORITE = "CLAP_PRESET_DISCOVERY_IS_FAVORITE"
    """
    This preset is a user's favorite
    """


