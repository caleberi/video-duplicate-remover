from re import I, compile
from shutil import move
from typing import List
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


class FolderTree:
    def __init__(self) -> None:
        self._dirs = []
        self._files = []

    @property
    def dirs(self):
        return self._dirs

    @property
    def files(self):
        return self._files

    @dirs.setter
    def dirs(self, path):
        self._dirs.append(resolve_os_encoding(path))

    @files.setter
    def files(self, path):
        self.files.append(resolve_os_encoding(path))


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
    tree = FolderTree()
    try:
        if not path:
            root_path = resolve_os_encoding(getcwd())
        else:
            root_path = resolve_os_encoding(path)

        queue = deque()

        queue.append(root_path)

        while queue:
            curr_dir_path = queue.popleft()
            with scandir(curr_dir_path) as dir_itr:
                for entry in dir_itr:
                    if entry.is_file():
                        tree.files = entry.path
                        continue
                    elif entry.is_dir():
                        tree.dirs = entry.path
                        queue.append(resolve_os_encoding(entry.path))

    except OSError as err:
        raise err
    else:
        return tree


def retrieve_filtered(filepaths: List[str], expression: str):
    """
    Filters provided list of filepath with regex
    :params  `filepaths` - list of file path to filter
    :params  `expresssion` - pattern to filter with
    """
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


def move_files_to_path(dst, src):
    """
    Relocates the file frorm src to dst
    :params `src` - source folder path
    :params `dst` - destination folder path
    """
    try:
        if not path.isdir(dst):
            raise FileNotFoundError(dst)
        move(src=src, dst=dst)
    except FileNotFoundError as file_not_found:
        raise IOError from file_not_found
    except IOError as err:
        raise err


def delete_folder(folder_path):
    """
    Delete the provide folder path
    :params `folder_path` - folder to delete
    """
    files = listdir(folder_path)
    for file in files:
        remove(path.join(folder_path, file))
    rmdir(folder_path)
