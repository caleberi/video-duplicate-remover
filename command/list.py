from os import getcwd, listdir, path

import click

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
    :params `folder_name` - path to list out
    """
    destination_folder_path = path.join(resolve_os_encoding(getcwd()), folder_name)
    files = listdir(destination_folder_path)
    print(f"::: FILES :${destination_folder_path}:::")
    for file in files:
        print(f"\t> {file}")
    print("> DONE .")
