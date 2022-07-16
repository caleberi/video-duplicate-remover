import click
from os import getcwd, listdir, path
from command.utils.helpers import resolve_os_encoding


@click.command()
@click.option(
    "-f",
    "--folder-name",
    default=".",
    help="the folder to list out",
)
def list_files_destination(folder_name):
    """
    List out all filepath that is in the folder
    
    :params `folder_name` - path to list out
    """
    destination_folder_path = path.join(resolve_os_encoding(getcwd()), folder_name)
    files = listdir(destination_folder_path)
    click.echo(f"::: FILES :${destination_folder_path}:::")
    for file in files:
        click.echo(f"\t> {file}")
    click.echo("> DONE .")
