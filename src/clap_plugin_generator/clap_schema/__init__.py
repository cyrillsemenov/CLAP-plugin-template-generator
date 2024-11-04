from pydantic import (
    SerializationInfo,
    SerializerFunctionWrapHandler,
    model_serializer,
    Field,
)
from typing import List, Dict, Any

from .base import Model, Extension
from .ext import AudioPort, AudioPorts, NotePort, NotePorts, Params, ParamInfo, State
from .plugin_descriptor import PluginDescriptor


class PluginData(Model):
    """
    Represents the metadata and configuration of a plugin.
    """

    plugin_prefix: str = Field(
        description="prefix for plugin used in a code",
        examples=["my_plugin"],
        pattern="[a-zA-Z_]+",
    )

    plugin_description: PluginDescriptor

    params: List[ParamInfo] = Field(examples=[ParamInfo.gain()])

    audio_ports: AudioPorts

    note_ports: NotePorts

    # plugin_extensions: List[Extensions] = Field(default_factory=list)
    # host_extensions: List[Extensions] = Field(default_factory=list)
    @model_serializer(mode="wrap")
    def mod_ser(self, handler: SerializerFunctionWrapHandler, info: SerializationInfo):
        params = Params(params=self.params).model_dump()
        dump: Dict[str, Any] = handler(self, info)
        dump.pop("params")
        plugin_extensions: List[Extension] = [
            params,
            dump.pop("audio_ports"),
            dump.pop("note_ports"),
            State(),
        ]
        host_extensions: List[Extension] = plugin_extensions
        dump.update(
            plugin_extensions=plugin_extensions, host_extensions=host_extensions
        )
        return dump


__all__ = [
    "AudioPort",
    "AudioPorts",
    "NotePort",
    "NotePorts",
    "Params",
    "ParamInfo",
    "PluginData",
    "PluginDescriptor",
]
