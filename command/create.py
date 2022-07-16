from os import makedirs, path

import click


@click.command()
@click.option(
    "-d", "--destination-path", help="the parent folder path to create", required=True
)
@click.option("-f", "--folder-name", help="the folder name to create ")
def create_folder_path(destination_path: str, folder_name: str) -> str:
    """
    Creates  a folder path using the specified destination path and folder name

    :params `destination_path` - the parent folder path to create
    :params `folder_name` - the folder name to create
    :returns the full destination path location
    """
    try:
        destination_folder_path = path.join(destination_path, folder_name)
        makedirs(destination_folder_path)
        click.echo(
            click.echo(
                f"created a folder at location : {destination_folder_path}", fg="green"
            )
        )
        return destination_folder_path
    except IOError:
        raise IOError
