from typing import List, Optional
from pydantic import Field
from ..base import Model, EnumList, Extension

from clap_plugin_generator.clap_data import (
    ClapAudioPort,
    ClapAudioPortType,
    ClapPluginExtensions,
)


class AudioPort(Model):
    """
    Represents an audio port, with properties such as:
    - `name`: The display name of the audio port.
    - `flags`: A list of flags indicating specific behaviors or requirements (e.g., main port).
    - `channel_count`: Number of channels (e.g., 0, 1, 2).
    - `port_type`: Type of the port (e.g., mono, stereo).
    - `in_place_pair`: Identifier for in-place processing support.

    Class Methods:
    - `stereo_in()`: Creates a stereo input port.
    - `stereo_out()`: Creates a stereo output port.
    - `mono_in()`: Creates a mono input port.
    - `mono_out()`: Creates a mono output port.
    """

    name: str = Field(description="displayable name", examples=["Stereo"])
    flags: int | EnumList[ClapAudioPort] = Field(default_factory=list, examples=[0])
    channel_count: Optional[int] = Field(ge=0, examples=[2])
    port_type: Optional[ClapAudioPortType] = Field(
        description="""If null or empty then it is unspecified (arbitrary audio).
This field can be compared against:
- CLAP_PORT_MONO
- CLAP_PORT_STEREO
- CLAP_PORT_SURROUND (defined in the surround extension)
- CLAP_PORT_AMBISONIC (defined in the ambisonic extension)

An extension can provide its own port type and way to inspect the channels.
""",
        examples=[ClapAudioPortType.STEREO],
    )
    in_place_pair: Optional[int | str] = Field(
        None,
        description="""in-place processing: allow the host to use the same buffer for input and output
if supported set the pair port id.
if not supported set to CLAP_INVALID_ID
""",
        examples=["CLAP_INVALID_ID"],
    )

    @classmethod
    def stereo_in(cls, name: str = "Stereo Input", main: bool = True, flags: list = []):
        """
        Creates a stereo input audio port.
        - `name`: Optional custom name for the audio port.
        - `main`: Whether the port is a main port (default True).
        - `flags`: Additional flags to be applied.
        """
        flags_set = set(flags)
        if main:
            flags_set.add(ClapAudioPort.IS_MAIN)
        return AudioPort(
            name=name,
            flags=list(flags_set),
            channel_count=2,
            port_type=ClapAudioPortType.STEREO,
        )

    @classmethod
    def stereo_out(
        cls, name: str = "Stereo Output", main: bool = True, flags: list = []
    ):
        """
        Creates a stereo output audio port.
        - `name`: Optional custom name for the audio port.
        - `main`: Whether the port is a main port (default True).
        - `flags`: Additional flags to be applied.
        """
        return AudioPort.stereo_in(name=name, main=main, flags=flags)

    @classmethod
    def mono_in(cls, name: str = "Mono Input", main: bool = True, flags: list = []):
        """
        Creates a mono input audio port.
        - `name`: Optional custom name for the audio port.
        - `main`: Whether the port is a main port (default True).
        - `flags`: Additional flags to be applied.
        """
        flags_set = set(flags)
        if main:
            flags_set.add(ClapAudioPort.IS_MAIN)
        return AudioPort(
            name=name,
            flags=list(flags_set),
            channel_count=2,
            port_type=ClapAudioPortType.MONO,
        )

    @classmethod
    def mono_out(cls, name: str = "Mono Output", main: bool = True, flags: list = []):
        """
        Creates a mono output audio port.
        - `name`: Optional custom name for the audio port.
        - `main`: Whether the port is a main port (default True).
        - `flags`: Additional flags to be applied.
        """
        return AudioPort.mono_in(name, main, flags)


class AudioPorts(Extension, extension_id=ClapPluginExtensions.AUDIO_PORTS):
    """
    Represents a collection of audio ports, including:
    - `input`: A list of input audio ports.
    - `output`: A list of output audio ports.
    """

    input: List[AudioPort] = Field(default_factory=list)
    output: List[AudioPort] = Field(default_factory=list)

    @classmethod
    def stereo_in_out(cls):
        return AudioPorts(
            input=[AudioPort.stereo_in()], output=[AudioPort.stereo_out()]
        )

    @classmethod
    def mono_in_out(cls):
        return AudioPorts(input=[AudioPort.mono_in()], output=[AudioPort.mono_out()])
