from collections import deque
import os
import queue
from typing import Any, Dict
import click
from os import getcwd, listdir, path, scandir
from command.utils.helpers import resolve_os_encoding
from pathlib import Path


"""
Main Directory/
├── Directory 1/
│   └── Directory 2/
│       ├── Directory 3/
│       │   └── Directory 4/
│       │       └── Hello World.txt
│       └── Say World.txt
├── Directory A/
│   └── Hmm.txt
├── directory-tree-print.cpp
├── letseee.txt
└── printTree.exe
"""


class TreeNode:
    def __init__(self, path_: str = None) -> None:
        self.node_tee_prefix = "├──"
        self.node_space_prefix = "   "
        self.node_elbow_prefix = "└──"
        self.symbol = path_
        self.name = None
        self.children: Dict[str, TreeNode] = {}
        self.isFile: bool = False
        self.isDir: bool = False
        self.isLink: bool = False
        self._metadata_update()

    def _generate_path_instance(self):
        return Path(self.symbol) if self.symbol is not None else None

    def _metadata_update(self):
        p = self._generate_path_instance()
        self.isFile = p.is_file()
        self.isDir = p.is_dir()
        self.isLink = p.is_symlink()
        self.name = p.name

    def _insert(self, path_: str):
        root = self
        p = Path(path_)

        if not p.is_relative_to(root.symbol) and not path_.startswith(root.symbol):
            raise ValueError(f"{path_} is not relative to the path {root.symbol}")

        suffix = path_.removeprefix(root.symbol)
        frags = suffix.split("/")[1:]

        i = 0
        p_ = root.symbol
        next_root_name = frags[i]
        while root:
            if next_root_name not in root.children:
                p_ = os.path.join(p_, next_root_name)
                root.children[next_root_name] = TreeNode(p_)
                break
            p_ = os.path.join(p_, next_root_name)
            root = root.children.get(next_root_name)
            i += 1
            next_root_name = frags[i]

    def _search(self, path_: str):
        root = self
        p = Path(path_)

        if not p.is_relative_to(root.symbol) and not path_.startswith(root.symbol):
            raise ValueError(f"{path_} is not relative to the path {root.symbol}")

        suffix = path_.removeprefix(root.symbol)
        frags = suffix.split("/")[1:]

        i = 0
        p_ = root.symbol
        next_root_name = frags[i]
        while root:
            if next_root_name not in root.children:
                return None
            p_ = os.path.join(p_, next_root_name)
            root = root.children.get(next_root_name)
            i += 1
            if i == len(frags):
                return root
            next_root_name = frags[i]
        return None

    def _print(self, width=0):
        root = self
        if width == 0:
            print(f"{self.node_space_prefix*width} 📁{root.name}")
        else:
            print(f"{self.node_space_prefix*width}{self.node_tee_prefix} 📁{root.name}")
        entities = sorted(
            [(k, v) for k, v in root.children.items()],
            key=lambda x: x[1].isDir,
            reverse=True,
        )
        l_entities = len(entities)
        for i, entry in enumerate(entities):
            frag, node = entry
            if node.isDir:
                node._print(width + 1)
            else:
                if i == l_entities - 1:
                    print(
                        f"{self.node_space_prefix*width}{self.node_elbow_prefix}🗒️ {frag}"
                    )
                else:
                    print(
                        f"{self.node_space_prefix*width}{self.node_tee_prefix}🗒️ {frag}"
                    )

    def __build__(self):
        d = resolve_os_encoding(self.symbol)
        tree = TreeNode(d)
        queue = deque()
        queue.append(d)

        while queue:
            curr = queue.popleft()
            with scandir(curr) as dir_itr:
                for entry in dir_itr:
                    if entry.is_dir():
                        queue.append(resolve_os_encoding(entry.path))
                    tree._insert(resolve_os_encoding(entry.path))
        return tree


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
    destination_folder_path = path.abspath(
        path.join(resolve_os_encoding(getcwd()), folder_name)
    )
    print(destination_folder_path)
    folder = TreeNode(destination_folder_path).__build__()
    folder._print()
    click.echo("> DONE .")
