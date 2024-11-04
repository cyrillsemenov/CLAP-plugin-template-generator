from typing import List, Optional, Any
from pydantic import Field
from ..base import Model, EnumList, Extension

from clap_plugin_generator.clap_data import ClapNoteDialect, ClapPluginExtensions


class NotePort(Model):
    """
    Represents a note port, with properties such as:
    - `name`: The display name of the note port.
    - `supported_dialects`: A list of supported note dialects (e.g., MIDI, CLAP).
    - `preferred_dialect`: Preferred note dialect for communication.

    Class Methods:
    - `midi_in()`: Creates a MIDI input note port.
    - `midi_out()`: Creates a MIDI output note port.
    """

    name: str = Field(description="displayable name")
    supported_dialects: EnumList[ClapNoteDialect] = Field(
        [ClapNoteDialect.MIDI],
        description="bitfield, see clap_note_dialect",
        examples=[[ClapNoteDialect.MIDI]],
    )
    preferred_dialect: Optional[ClapNoteDialect] = Field(
        None,
        description="One value of clap_note_dialect. By default the first member of supported_dialects list.",
        examples=[ClapNoteDialect.MIDI],
    )

    def model_post_init(self, __context: Any) -> None:
        if self.preferred_dialect is None:
            self.preferred_dialect = self.supported_dialects[0]
        return super().model_post_init(__context)

    @classmethod
    def midi_in(cls, name: str = "MIDI Input", dialects: list = []):
        """
        Creates a MIDI input note port.
        - `name`: Optional custom name for the note port.
        - `dialects`: Additional supported dialects to be applied.
        """
        dialects_set = set([ClapNoteDialect.MIDI, *dialects])
        return NotePort(
            name=name, supported_dialects=list(dialects_set), preferred_dialect=None
        )

    @classmethod
    def midi_out(cls, name: str = "MIDI Output", dialects: list = []):
        """
        Creates a MIDI output note port.
        - `name`: Optional custom name for the note port.
        - `dialects`: Additional supported dialects to be applied.
        """
        return NotePort.midi_in(name, dialects)


class NotePorts(Extension, extension_id=ClapPluginExtensions.NOTE_PORTS):
    """
    Represents a collection of note ports, including:
    - `input`: A list of input note ports.
    - `output`: A list of output note ports.
    """

    input: List[NotePort] = Field(default_factory=list)
    output: List[NotePort] = Field(default_factory=list)

    @classmethod
    def midi_in_out(cls, mpe: bool = False):
        dialects = []
        if mpe:
            dialects.append(ClapNoteDialect.MIDI_MPE)
        return NotePorts(
            input=[NotePort.midi_in(dialects=dialects)],
            output=[NotePort.midi_out(dialects=dialects)],
        )
