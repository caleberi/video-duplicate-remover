import os
from re import I
import click
from command.utils.helpers import (
    PathNotFoundError,
    delete_folder,
    move_files_to_path,
)
from command.utils.helpers import (
    create_destination_folder,
    retreive_all_files_path,
    retrieve_filtered,
)


@click.command()
@click.option(
    "-f",
    "--folder-path",
    help="the video folder path to clean up",
    required=True,
)
@click.option(
    "-o", "--out", help="the output folder path to store duplicates ", required=True
)
@click.option("-r", "--regex", help="filter pattern for movies")
@click.option("-d", "--delete-output", help="delete the copies", is_flag=True)
def clean(folder_path: str, out: str, regex: str, delete_output: bool):
    """
    Remove all video files from a folder 
    
    :params `folder_path` - path to clean
    :params `out` - output folder path
    :params `regex` - regular expression pattern
    :params  `delete_output` - flag to delete the output folder
    """
    try:
        filepaths = retreive_all_files_path(folder_path).files
        regex = r""
        if len(filepaths):
            if regex:
                expression = rf"{regex}"
            else:
                expression = r"""((\s)?copy( \d*)?.[a-zA-Z]{1,4}([0-9]*))$|
                [0-9A-Fa-f]*.[a-zA-Z]{1,4} copy( \d*)?.[a-zA-Z]{1,4}$|
                [0-9a-zA-Z]*.[a-zA-Z]{1,4} copy( \d*)?.[a-zA-Z]{1,4}$|
                (\w+(\s|_|-)*)*(.[a-zA-Z]{1,4})? copy( \d*)?.[a-zA-Z]{1,4}$|
                (\w+(\s|_|-)*)*(_|\s)(\(\d+\)|\d+)\.[a-zA-Z]{1,4}$"""

            filtered_filepaths = retrieve_filtered(filepaths, expression)
            if not os.path.exists(out):
                destination_folder_path = create_destination_folder(out)
            for file_path in filtered_filepaths:
                move_files_to_path(destination_folder_path, file_path)
            if delete_output:
                delete_folder(folder_path=destination_folder_path)

    except PathNotFoundError as path_not_found:
        print(path_not_found.strerror)
    except FileNotFoundError as file_not_found:
        print(file_not_found.strerror)
    except IOError as io_error:
        print(io_error.strerror)
