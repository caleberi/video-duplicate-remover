from os import listdir, path, remove, rmdir
import click


@click.command()
@click.option("-f", "--folder", help="the path to delete ")
def delete_folder(folder):
    """
    Delete the provide folder path

    :params folder_path - folder to delete
    """
    dir_list = listdir(folder)
    for path_ in dir_list:
        remove(path.join(folder, path_))
    rmdir(folder)
