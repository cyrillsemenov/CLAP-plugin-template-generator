from typing import List
from pydantic import Field
from ..base import Model, EnumList, Extension

from clap_plugin_generator.clap_data import ClapParam, ClapPluginExtensions


class ParamInfo(Model):
    """
    Represents information about a parameter, including:
    - `name`: Name of the parameter.
    - `module`: Module that the parameter belongs to.
    - `info_flags`: Flags that represent additional information about the parameter.
    - `min_value`: Minimum value for the parameter.
    - `max_value`: Maximum value for the parameter.
    - `default_value`: Default value of the parameter.
    - `pattern`: Optional pattern for formatting the parameter value.
    """

    name: str = Field(
        description="""The display name. eg: "Volume". This does not need to be unique. Do not include the module
text in this. The host should concatenate/format the module + name in the case where showing
the name alone would be too vague.
""",
        examples=["Volume"],
    )
    module: str = Field(
        description="""The module path containing the param, eg: "Oscillators/Wavetable 1".
'/' will be used as a separator to show a tree-like structure.
""",
        examples="VCA",
    )
    info_flags: EnumList[ClapParam] = Field(default_factory=list)
    min_value: float = Field(description="Minimum plain value", examples=[0])
    max_value: float = Field(description="Maximum plain value", examples=[1])
    default_value: float = Field(description="Default plain value", examples=[1])
    pattern: str = Field(
        pattern=".*%([-+#0])?(\d+|\*)?(?:\.(\d+|\*))?([hljztL]|hh|ll)?[diuoxXfFeEgGaAcspn].*",
        examples=["Val: %f"],
    )

    @classmethod
    def gain(cls):
        return ParamInfo(
            name="gain",
            module="dynamics",
            min_value=0.0,
            max_value=1.0,
            default_value=0.5,
            pattern="%.2f",
        )

    @classmethod
    def frequency(cls):
        return ParamInfo(
            name="frequency",
            module="oscillator",
            min_value=20.0,
            max_value=20000.0,
            default_value=440.0,
            pattern="%f",
        )

    @classmethod
    def resonance(cls):
        return ParamInfo(
            name="resonance",
            module="filter",
            min_value=0.1,
            max_value=10.0,
            default_value=1.0,
            pattern="%.2f",
        )

    @classmethod
    def pan(cls):
        return ParamInfo(
            name="pan",
            module="mixer",
            min_value=-1.0,
            max_value=1.0,
            default_value=0.0,
            pattern="%.2f",
        )

    @classmethod
    def attack(cls):
        return ParamInfo(
            name="attack",
            module="envelope",
            min_value=0.0,
            max_value=5.0,
            default_value=0.1,
            pattern="%.3f",
        )


class Params(Extension, extension_id=ClapPluginExtensions.PARAMS):
    params: List[ParamInfo]

    @classmethod
    def example(cls) -> "Params":
        return Params(
            params=[
                ParamInfo.gain(),
                ParamInfo.frequency(),
                ParamInfo.attack(),
            ]
        )
