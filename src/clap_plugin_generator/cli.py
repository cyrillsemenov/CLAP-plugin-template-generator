import json
import os
import pathlib
import sys
from typing import Optional, TextIO
from clap_plugin_generator.clap_schema import PluginData
from pydantic_yaml import parse_yaml_raw_as

import jinja2
import click

SCRIPT_ROOT = pathlib.Path(__file__).parent.resolve()
CWD = pathlib.Path().parent.resolve()
TEMPLATE_SUFFIX = ".j2"
JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(f"{SCRIPT_ROOT}/templates"),
    extensions=["jinja2_strcase.StrcaseExtension"],
)


@click.group()
@click.pass_context
def cli(ctx: click.Context):
    """CLI for generating JSON schemas and rendering project templates."""
    # if ctx.invoked_subcommand is None:
    #     click.echo("I was invoked without subcommand")
    # else:
    #     click.echo(f"I am about to invoke {ctx.invoked_subcommand}")
    pass


@cli.command()
@click.argument("filename", default=sys.stdout, type=click.File("w"))
@click.option(
    "--indent", help="The number of spaces to use for JSON indentation", default=2
)
def generate_schema(filename: TextIO, indent: int) -> None:
    """Generate and output JSON schema.

    FILENAME specifies the path where the schema will be saved.
    If not provided, the schema is printed to stdout.
    """
    click.secho(message="Generating JSON schema...", file=sys.stderr, fg="cyan")
    plugin_data_schema = PluginData.model_json_schema()
    message = json.dumps(plugin_data_schema, indent=indent)
    click.echo(
        message=message,
        file=filename,
    )


@cli.command()
@click.pass_obj
@click.argument("file", type=click.File("r"))
@click.argument("output", default=sys.stdout, type=click.File("w"))
@click.option(
    "--data",
    help="Path to a YAML file with data for rendering the template. Uses default values if omitted.",
    type=click.File("r"),
    default=f"{SCRIPT_ROOT}/sample.yaml",
)
def render_template(
    obj: Optional[PluginData], file: TextIO, output: TextIO, data: TextIO
) -> None:
    """Render a single template using provided data.

    FILE is the template file to read and render.

    OUTPUT specifies the output file where rendered content is saved.
    Defaults to stdout.
    """
    if obj is None:
        obj = parse_yaml_raw_as(PluginData, data)

    template = JINJA_ENV.from_string(file.read())
    rendered_code = template.render(obj.model_dump())
    output.write(rendered_code)


@cli.command()
@click.pass_context
@click.argument(
    "output",
    type=click.Path(file_okay=False, resolve_path=True, writable=True),
    required=False,
)
@click.option(
    "--data",
    help="Path to a YAML file with data for rendering the template. Uses default values if omitted.",
    type=click.File("r"),
    default=f"{SCRIPT_ROOT}/sample.yaml",
)
@click.option(
    "--template-path",
    help="Directory path for template files used in rendering.",
    type=click.Path(exists=True, file_okay=False, resolve_path=True),
    required=True,
    default=f"{SCRIPT_ROOT}/templates/clap",
)
def render(
    ctx: click.Context, output: Optional[str], template_path: str, data: TextIO
) -> None:
    """Render templates to create a new project.

    OUTPUT specifies the path where the rendered project will be stored.
    If not provided, it defaults to the plugin's prefix.
    """
    plugin_data = parse_yaml_raw_as(PluginData, data)
    ctx.obj = plugin_data

    if output is None:
        output = os.path.join(CWD, plugin_data.plugin_prefix)

    for template_dir, _, files in os.walk(template_path):
        for file in files:
            output_dir = os.path.join(
                output, template_dir.removeprefix(template_path).lstrip("/\\")
            )
            os.makedirs(output_dir, exist_ok=True)

            with (
                open(os.path.join(template_dir, file), "r") as template_file,
                open(
                    os.path.join(output_dir, file.removesuffix(TEMPLATE_SUFFIX)), "w"
                ) as output_file,
            ):
                ctx.invoke(render_template, file=template_file, output=output_file)


if __name__ == "__main__":
    cli()
