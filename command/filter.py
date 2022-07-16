import click
from os import path
from re import I, compile, Pattern
from command.utils.helpers import retreive_all_files_path


def match(filepath: str, pattern: Pattern):
    filename = path.basename(filepath)
    return pattern.search(filename) != None


@click.command()
@click.option("-f", "--folder-path", help="the path to delete ", required=True)
@click.option("-r", "--regex", help="regex pattern to use")
@click.option("-p", "--print_", help="print out files", is_flag=True)
def retrieve_filtered(folder_path: str, regex: str, print_: bool):
    """
    Filter files based on provided regex expression and print it

    :params `folder_path`  - path to retrieved  and filter from
    :params `regex` - regular expression pattern
    """
    filepaths = retreive_all_files_path(folder_path)
    filtered = []
    expression = r""
    if regex:
        expression = rf"{regex}"
    else:
        expression = r"""((\s)?copy( \d*)?.[a-zA-Z]{1,4}([0-9]*))$|
        [0-9A-Fa-f]*.[a-zA-Z]{1,4} copy( \d*)?.[a-zA-Z]{1,4}$|
        [0-9a-zA-Z]*.[a-zA-Z]{1,4} copy( \d*)?.[a-zA-Z]{1,4}$|
        (\w+(\s|_|-)*)*(.[a-zA-Z]{1,4})? copy( \d*)?.[a-zA-Z]{1,4}$|
        (\w+(\s|_|-)*)*(_|\s)(\(\d+\)|\d+)\.[a-zA-Z]{1,4}$"""

    r = compile(expression, I)
    for filepath in filepaths:
        if match(filepath, r):
            if print_:
                click.echo(click.echo(f"> {filepath}", fg="green"))
            filtered.append(filepath)
    return filtered
