from pydantic import Field, AnyUrl

from .base import Model, EnumList

from ..clap_data import ClapPluginFeatures


class PluginDescriptor(Model):
    """
    Mandatory fields must be set and must not be blank.
    Otherwise the fields can be null or blank, though it is safer to make them blank.

    Some indications regarding id and version
    - id is an arbitrary string which should be unique to your plugin,
      we encourage you to use a reverse URI eg: "com.u-he.diva"
    - version is an arbitrary string which describes a plugin,
      it is useful for the host to understand and be able to compare two different
      version strings, so here is a regex like expression which is likely to be
      understood by most hosts: MAJOR(.MINOR(.REVISION)?)?( (Alpha|Beta) XREV)?
    """

    id: str = Field(
        pattern="\S+\.\S+\.\S+",
        examples=["com.your-company.YourPlugin"],
    )
    name: str = Field(
        examples=["Plugin Name"],
    )
    vendor: str = Field(
        examples=["Vendor"],
    )
    url: AnyUrl = Field(
        examples=["https://your-domain.com/your-plugin"],
    )
    manual_url: AnyUrl = Field(
        examples=["https://your-domain.com/your-plugin/manual"],
    )
    support_url: AnyUrl = Field(
        examples=["https://your-domain.com/support"],
    )
    version: str = Field(
        pattern="\d+(\.\d+(\.\d+)?)?( ?\w+)?",
        examples=["1.4.2"],
    )
    description: str = Field(examples=["The plugin description."])
    features: EnumList[ClapPluginFeatures] = Field(
        description="""Arbitrary list of keywords.
They can be matched by the host indexer and used to classify the plugin.
The array of pointers must be null terminated.
For some standard features see plugin-features.h""",
    )
