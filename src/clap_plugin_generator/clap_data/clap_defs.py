"""
This file was automatically generated from CLAP API headers
by 'CLAP Data Parser' tool

CLAP: https://github.com/free-audio/clap/
CLAP Data Parser: https://github.com/cyrillsemenov/CLAP-plugin-template-generator/utils/parse_clap_enums.c

Date: 2024-11-02 15:51
"""

from enum import StrEnum


class ClapVersion(StrEnum):
    MAJOR = "CLAP_VERSION_MAJOR"
    """
    1
    """

    MINOR = "CLAP_VERSION_MINOR"
    """
    2
    """

    REVISION = "CLAP_VERSION_REVISION"
    """
    2
    """



class ClapPluginFeatures(StrEnum):
    INSTRUMENT = "CLAP_PLUGIN_FEATURE_INSTRUMENT"
    """
    "instrument"
    """

    AUDIO_EFFECT = "CLAP_PLUGIN_FEATURE_AUDIO_EFFECT"
    """
    "audio-effect"
    """

    NOTE_EFFECT = "CLAP_PLUGIN_FEATURE_NOTE_EFFECT"
    """
    "note-effect"
    """

    NOTE_DETECTOR = "CLAP_PLUGIN_FEATURE_NOTE_DETECTOR"
    """
    "note-detector"
    """

    ANALYZER = "CLAP_PLUGIN_FEATURE_ANALYZER"
    """
    "analyzer"
    """

    SYNTHESIZER = "CLAP_PLUGIN_FEATURE_SYNTHESIZER"
    """
    "synthesizer"
    """

    SAMPLER = "CLAP_PLUGIN_FEATURE_SAMPLER"
    """
    "sampler"
    """

    DRUM = "CLAP_PLUGIN_FEATURE_DRUM"
    """
    "drum" // For single drum
    """

    DRUM_MACHINE = "CLAP_PLUGIN_FEATURE_DRUM_MACHINE"
    """
    "drum-machine"
    """

    FILTER = "CLAP_PLUGIN_FEATURE_FILTER"
    """
    "filter"
    """

    PHASER = "CLAP_PLUGIN_FEATURE_PHASER"
    """
    "phaser"
    """

    EQUALIZER = "CLAP_PLUGIN_FEATURE_EQUALIZER"
    """
    "equalizer"
    """

    DEESSER = "CLAP_PLUGIN_FEATURE_DEESSER"
    """
    "de-esser"
    """

    PHASE_VOCODER = "CLAP_PLUGIN_FEATURE_PHASE_VOCODER"
    """
    "phase-vocoder"
    """

    GRANULAR = "CLAP_PLUGIN_FEATURE_GRANULAR"
    """
    "granular"
    """

    FREQUENCY_SHIFTER = "CLAP_PLUGIN_FEATURE_FREQUENCY_SHIFTER"
    """
    "frequency-shifter"
    """

    PITCH_SHIFTER = "CLAP_PLUGIN_FEATURE_PITCH_SHIFTER"
    """
    "pitch-shifter"
    """

    DISTORTION = "CLAP_PLUGIN_FEATURE_DISTORTION"
    """
    "distortion"
    """

    TRANSIENT_SHAPER = "CLAP_PLUGIN_FEATURE_TRANSIENT_SHAPER"
    """
    "transient-shaper"
    """

    COMPRESSOR = "CLAP_PLUGIN_FEATURE_COMPRESSOR"
    """
    "compressor"
    """

    EXPANDER = "CLAP_PLUGIN_FEATURE_EXPANDER"
    """
    "expander"
    """

    GATE = "CLAP_PLUGIN_FEATURE_GATE"
    """
    "gate"
    """

    LIMITER = "CLAP_PLUGIN_FEATURE_LIMITER"
    """
    "limiter"
    """

    FLANGER = "CLAP_PLUGIN_FEATURE_FLANGER"
    """
    "flanger"
    """

    CHORUS = "CLAP_PLUGIN_FEATURE_CHORUS"
    """
    "chorus"
    """

    DELAY = "CLAP_PLUGIN_FEATURE_DELAY"
    """
    "delay"
    """

    REVERB = "CLAP_PLUGIN_FEATURE_REVERB"
    """
    "reverb"
    """

    TREMOLO = "CLAP_PLUGIN_FEATURE_TREMOLO"
    """
    "tremolo"
    """

    GLITCH = "CLAP_PLUGIN_FEATURE_GLITCH"
    """
    "glitch"
    """

    UTILITY = "CLAP_PLUGIN_FEATURE_UTILITY"
    """
    "utility"
    """

    PITCH_CORRECTION = "CLAP_PLUGIN_FEATURE_PITCH_CORRECTION"
    """
    "pitch-correction"
    """

    RESTORATION = "CLAP_PLUGIN_FEATURE_RESTORATION"
    """
    "restoration" // repair the sound
    """

    MULTI_EFFECTS = "CLAP_PLUGIN_FEATURE_MULTI_EFFECTS"
    """
    "multi-effects"
    """

    MIXING = "CLAP_PLUGIN_FEATURE_MIXING"
    """
    "mixing"
    """

    MASTERING = "CLAP_PLUGIN_FEATURE_MASTERING"
    """
    "mastering"
    """

    MONO = "CLAP_PLUGIN_FEATURE_MONO"
    """
    "mono"
    """

    STEREO = "CLAP_PLUGIN_FEATURE_STEREO"
    """
    "stereo"
    """

    SURROUND = "CLAP_PLUGIN_FEATURE_SURROUND"
    """
    "surround"
    """

    AMBISONIC = "CLAP_PLUGIN_FEATURE_AMBISONIC"
    """
    "ambisonic"
    """


