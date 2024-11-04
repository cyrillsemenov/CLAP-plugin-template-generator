from pydantic import (
    BaseModel,
    ConfigDict,
    PrivateAttr,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    model_serializer,
)
from pydantic.functional_validators import AfterValidator
from typing import Any, Dict, List, TypeVar
from typing_extensions import Annotated
from enum import Enum

from ..clap_data import ClapHostExtensions, ClapPluginExtensions


def get_val(a: Enum | str) -> Any:
    if isinstance(a, str):
        return a
    return a.value


T = TypeVar("T")
EnumList = List[Annotated[T, AfterValidator(get_val)]]


class Model(BaseModel):
    model_config = ConfigDict(
        use_enum_values=True,
        validate_default=True,
        validate_assignment=True,
    )


class Extension(Model):
    _extension_id: ClapPluginExtensions | ClapHostExtensions = PrivateAttr()

    def __init_subclass__(cls, **kwargs: ConfigDict):
        cls._extension_id = kwargs.pop("extension_id")
        return super().__init_subclass__()

    @model_serializer(mode="wrap")
    def mod_ser(self, handler: SerializerFunctionWrapHandler, info: SerializationInfo):
        dump: Dict[str, Any] = handler(self, info)
        dump.update(extension_id=str(self._extension_id))
        return dump
