from re import I, compile
from shutil import move
import click
from collections import deque
from os import (
    F_OK,
    W_OK,
    access,
    fsdecode,
    getcwd,
    listdir,
    mkdir,
    path,
    name as os_name,
    remove,
    rmdir,
    scandir,
)
from sys import getfilesystemencoding

from command.create import create_folder_path


class PathNotFoundError(FileNotFoundError):
    def __init__(self, path_) -> None:
        super().__init__()
        self.path = path_

    def __str__(self) -> str:
        return f"The provided path :{self.path} with does not exist "


def get_file_extension(path):
    return path.splitext(path)[-1]


def get_root_dir():
    return "/" if os_name == "postfix" else "C:\\"


def resolve_os_encoding(path_):
    return fsdecode(path_) if getfilesystemencoding() != "utf-8" else path_


def create_destination_folder(folder_name):
    destination_path = resolve_os_encoding(getcwd())
    try:
        if not access(destination_path, F_OK):
            raise PathNotFoundError(destination_path)
        if not access(destination_path, W_OK):
            raise PermissionError()
    except PathNotFoundError:
        create_folder_path(destination_path, folder_name)
    except PermissionError as permission_denied:
        raise permission_denied
    else:
        try:
            destination_folder_path = path.join(destination_path, folder_name)
            if not path.exists(destination_folder_path) or not path.isdir(
                destination_folder_path
            ):
                mkdir(destination_folder_path)
            if not path.isdir(destination_path):
                raise FileNotFoundError()
            return destination_folder_path
        except IOError as err:
            raise err


def retreive_all_files_path(path):
    filepaths = []
    try:
        # get the current working directory
        if not path:
            root_path = resolve_os_encoding(getcwd())
        else:
            root_path = resolve_os_encoding(path)

        click.echo(
            "Queuing directories / sub-directories path for file path processing"
        )
        # retrieve all the available files names and path
        queue = deque()
        queue.append(root_path)
        # open all subdirectories in current folder by adding them
        while queue:
            curr_dir_path = queue.popleft()
            with scandir(curr_dir_path) as dir_itr:
                for entry in dir_itr:
                    if entry.is_file():
                        filepaths.append(resolve_os_encoding(entry.path))
                        continue
                    elif entry.is_dir():
                        queue.append(resolve_os_encoding(entry.path))
    except OSError as err:
        click.echo(
            "Queuing directories / sub-directories" + " path for file path processing"
        )
        raise err
    else:
        return filepaths


def retrieve_filtered(filepaths, expression):
    try:
        filtered = []
        c = compile(expression, I)
        for filepath in filepaths:
            filename = path.basename(filepath)
            if c.search(filename):
                filtered.append(filepath)
        return filtered
    except Exception as e:
        raise e


def move_files_to_path(destination_path, file_path):
    file_name = path.basename(file_path)
    try:
        if not path.isdir(destination_path):
            raise FileNotFoundError(destination_path)
        move(file_path, destination_path)
        print(f"moved the file : {file_name} into the folder in {destination_path} ")
    except FileNotFoundError as file_not_found:
        print(f"The destination folder : {file_not_found.args[0]} was not found.")
        raise IOError from file_not_found
    except IOError as err:
        print(
            f"error occured while trying to move file : {file_name} to {destination_path}"
        )
        raise err


def delete_folder(folder_path):
    """
    delete the provide folder path
    :params folder_path - folder to delete
    """
    files = listdir(folder_path)
    for file in files:
        click.echo(f"deleting file : {file} ")
        remove(path.join(folder_path, file))
    rmdir(folder_path)
