from .audio_ports import AudioPorts, AudioPort
from .note_ports import NotePorts, NotePort
from .params import Params, ParamInfo

from ..base import Extension
from clap_plugin_generator.clap_data import ClapPluginExtensions


class State(Extension, extension_id=ClapPluginExtensions.STATE):
    pass


Extensions = AudioPorts | NotePorts | Params | State

__all__ = [
    "Extensions",
    "AudioPorts",
    "NotePorts",
    "Params",
    "AudioPort",
    "NotePort",
    "ParamInfo",
    "State",
]
