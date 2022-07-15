from os import listdir, path, remove, rmdir
import click


@click.command()
@click.option("-f", "--folder-path", help="the path to delete ")
def delete_folder(folder_path):
    """
    Delete the provide folder path
    
    :params folder_path - folder to delete
    """
    files = listdir(folder_path)
    for file in files:
        click.echo(f"deleting file : {file} ")
        remove(path.join(folder_path, file))
    rmdir(folder_path)
