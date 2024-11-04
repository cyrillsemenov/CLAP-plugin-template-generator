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
YAML_SAMPLE_PATH = f"{SCRIPT_ROOT}/sample.yaml"
TEMPLATE_DIR = f"{SCRIPT_ROOT}/templates/clap"
JINJA_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(f"{SCRIPT_ROOT}/templates"),
    extensions=["jinja2_strcase.StrcaseExtension"],
)


def log_info(message: str):
    click.secho(message, fg="cyan", file=sys.stderr)


def log_success(message: str):
    click.secho(message, fg="green", file=sys.stderr)


def log_warning(message: str):
    click.secho(message, fg="yellow", file=sys.stderr)


def log_error(message: str):
    click.secho(message, fg="red", err=True, file=sys.stderr)


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
def generate_json_schema(filename: TextIO, indent: int) -> None:
    """Generate and output JSON schema.

    FILENAME specifies the path where the schema will be saved.
    If not provided, the schema is printed to stdout.
    """
    try:
        plugin_data_schema = PluginData.model_json_schema()
        message = json.dumps(plugin_data_schema, indent=indent)
        click.echo(
            message=message,
            file=filename,
        )
        log_success("JSON schema generation completed successfully.")
    except Exception as e:
        log_error(f"Failed to generate JSON schema: {str(e)}")


@cli.command()
@click.argument("filename", default=sys.stdout, type=click.File("w"))
def sample_data(filename: TextIO, indent: int) -> None:
    """Generate and output sample YAML content.

    FILENAME specifies the path where the sample YAML content will be saved.
    If not provided, the content is printed to stdout.
    """
    try:
        with open(YAML_SAMPLE_PATH, "r") as sample:
            click.echo(
                message=sample.read(),
                file=filename,
            )
        log_success("Sample YAML data generated successfully.")
    except FileNotFoundError:
        log_error(f"Sample YAML file not found at path: {YAML_SAMPLE_PATH}")
    except Exception as e:
        log_error(f"Failed to generate sample data: {str(e)}")


@cli.command()
@click.pass_obj
@click.argument("file", type=click.File("r"))
@click.argument("output", default=sys.stdout, type=click.File("w"))
@click.option(
    "--data",
    help="Path to a YAML file with data for rendering the template. Uses default values if omitted.",
    type=click.File("r"),
    default=YAML_SAMPLE_PATH,
)
def render_single_template(
    obj: Optional[PluginData], file: TextIO, output: TextIO, data: TextIO
) -> None:
    """Render a single template using provided data.

    FILE is the template file to read and render.

    OUTPUT specifies the output file where rendered content is saved.
    Defaults to stdout.
    """
    try:
        log_success_on = False
        if obj is None:
            log_success_on = True
            obj = parse_yaml_raw_as(PluginData, data)

        template = JINJA_ENV.from_string(file.read())
        rendered_code = template.render(obj.model_dump())
        output.write(rendered_code)
        if log_success_on:
            log_success(f"Template rendered successfully: {file.name}")
    except jinja2.TemplateError as e:
        log_error(f"Failed to render template '{file.name}': {str(e)}")
    except Exception as e:
        log_error(f"Unexpected error rendering template '{file.name}': {str(e)}")


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
    default=YAML_SAMPLE_PATH,
)
@click.option(
    "--template-path",
    help="Directory path for template files used in rendering.",
    type=click.Path(exists=True, file_okay=False, resolve_path=True),
    required=True,
    default=TEMPLATE_DIR,
)
def render(
    ctx: click.Context, output: Optional[str], template_path: str, data: TextIO
) -> None:
    """Render templates to create a new project.

    OUTPUT specifies the path where the rendered project will be stored.
    If not provided, it defaults to the plugin's prefix.
    """
    try:
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
                template_name = file.removesuffix(TEMPLATE_SUFFIX)
                with (
                    open(os.path.join(template_dir, file), "r") as template_file,
                    open(os.path.join(output_dir, template_name), "w") as output_file,
                ):
                    log_info(f"Rendering template: {file}")
                    ctx.invoke(
                        render_single_template, file=template_file, output=output_file
                    )
        log_success("Project templates rendered successfully.")
    except FileNotFoundError as e:
        log_error(f"File not found: {str(e)}")
    except Exception as e:
        log_error(f"Failed to render project templates: {str(e)}")


if __name__ == "__main__":
    cli()
