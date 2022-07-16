import click
from command.clean import clean
from command import create, list, filter as filter_, delete


@click.group()
def cli():
    pass


cli.add_command(create.create_folder_path, "create")
cli.add_command(list.list_files_destination, "list")
cli.add_command(filter_.retrieve_filtered, "filter")
cli.add_command(delete.delete_folder, "delete")
cli.add_command(clean, "clean")
