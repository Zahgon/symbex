import ast
import click
import csv
import dataclasses
import importlib
import inspect
import json
import pathlib
import site
import subprocess
import sys
from typing import TextIO, Iterable, Literal, Tuple

from .lib import (
    code_for_node,
    find_symbol_nodes,
    import_line_for_function,
    read_file,
    type_summary,
)


@dataclasses.dataclass


@dataclasses.dataclass
class Output:
    symbol_id: str
    output_identifier_line: str
    output_import_line: str
    snippet: str


@click.command()
@click.version_option()
@click.argument("symbols", nargs=-1)
@click.option(
    "files",
    "-f",
    "--file",
    type=click.Path(file_okay=True, dir_okay=False),
    multiple=True,
    help="Files to search",
)
@click.option(
    "directories",
    "-d",
    "--directory",
    type=click.Path(file_okay=False, dir_okay=True, resolve_path=True),
    multiple=True,
    help="Directories to search",
)
@click.option("--stdlib", is_flag=True, help="Search the Python standard library")
@click.option(
    "excludes",
    "-x",
    "--exclude",
    type=click.Path(file_okay=False, dir_okay=True, resolve_path=True),
    multiple=True,
    help="Directories to exclude",
)
@click.option(
    "-s",
    "--signatures",
    is_flag=True,
    help="Show just function and class signatures",
)
@click.option(
    "-n",
    "--no-file",
    is_flag=True,
    help="Don't include the # File: comments in the output",
)
@click.option(
    "-i",
    "--imports",
    is_flag=True,
    help="Show 'from x import y' lines for imported symbols",
)
@click.option(
    "modules", "-m", "--module", multiple=True, help="Modules to search within"
)
@click.option(
    "sys_paths",
    "--sys-path",
    multiple=True,
    help="Calculate imports relative to these on sys.path",
)
@click.option(
    "--docs",
    "--docstrings",
    is_flag=True,
    help="Show function and class signatures plus docstrings",
)
@click.option(
    "--count",
    is_flag=True,
    help="Show count of matching symbols",
)
@click.option(
    "--silent",
    is_flag=True,
    help="Silently ignore Python files with parse errors",
)
@click.option(
    "--function",
    is_flag=True,
    help="Filter functions",
)
@click.option(
    "async_",
    "--async",
    is_flag=True,
    help="Filter async functions",
)
@click.option(
    "unasync",
    "--unasync",
    is_flag=True,
    help="Filter non-async functions",
)
@click.option(
    "class_",
    "--class",
    is_flag=True,
    help="Filter classes",
)
@click.option(
    "--documented",
    is_flag=True,
    help="Filter functions with docstrings",
)
@click.option(
    "--undocumented",
    is_flag=True,
    help="Filter functions without docstrings",
)
@click.option(
    "--public",
    is_flag=True,
    help="Filter for symbols without a _ prefix",
)
@click.option(
    "--private",
    is_flag=True,
    help="Filter for symbols with a _ prefix",
)
@click.option(
    "--dunder",
    is_flag=True,
    help="Filter for symbols matching __*__",
)
@click.option(
    "--typed",
    is_flag=True,
    help="Filter functions with type annotations",
)
@click.option(
    "--untyped",
    is_flag=True,
    help="Filter functions without type annotations",
)
@click.option(
    "--partially-typed",
    is_flag=True,
    help="Filter functions with partial type annotations",
)
@click.option(
    "--fully-typed",
    is_flag=True,
    help="Filter functions with full type annotations",
)
@click.option(
    "--no-init",
    is_flag=True,
    help="Filter to exclude any __init__ methods",
)
@click.option(
    "--check", is_flag=True, help="Exit with non-zero code if any matches found"
)
@click.option(
    "--replace",
    is_flag=True,
    help="Replace matching symbol with text from stdin",
)
@click.option("--rexec", help="Replace with the result of piping to this tool")
# Output options
@click.option("csv_", "--csv", is_flag=True, help="Output as CSV")
@click.option("--tsv", is_flag=True, help="Output as TSV")
@click.option("json_", "--json", is_flag=True, help="Output as JSON")
@click.option("--nl", is_flag=True, help="Output as newline-delimited JSON")
@click.option("--id-prefix", help="Prefix to use for symbol IDs")
def cli(
    symbols,
    files,
    directories,
    stdlib,
    excludes,
    signatures,
    no_file,
    imports,
    modules,
    sys_paths,
    docs,
    count,
    silent,
    function,
    async_,
    unasync,
    class_,
    documented,
    undocumented,
    public,
    private,
    dunder,
    typed,
    untyped,
    partially_typed,
    fully_typed,
    no_init,
    check,
    replace,
    rexec,
    csv_,
    tsv,
    json_,
    nl,
    id_prefix,
):
    """
    Find symbols in Python code and print the code for them.

    Example usage:

    \b
        # Search current directory and subdirectories
        symbex my_function MyClass

    \b
        # Search using a wildcard
        symbex 'test_*'

    \b
        # Find a specific class method
        symbex 'MyClass.my_method'

    \b
        # Find class methods using wildcards
        symbex '*View.handle_*'

    \b
        # Search a specific file
        symbex MyClass -f my_file.py

    \b
        # Search within a specific directory and its subdirectories
        symbex Database -d ~/projects/datasette

    \b
        # View signatures for all symbols in current directory and subdirectories
        symbex -s

    \b
        # View signatures for all test functions
        symbex 'test_*' -s

    \b
        # View signatures for all async functions with type definitions
        symbex --async --typed -s

    \b
        # Count the number of --async functions in the project
        symbex --async --count

    \b
        # Replace my_function with a new implementation:
        echo "def my_function(a, b):
            # This is a replacement implementation
            return a + b + 3
        " | symbex my_function --replace

    \b
        # Replace my_function with the output of a command:
        symbex first_function --rexec "sed 's/^/# /'"
        # This uses sed to comment out the function body
    """
    pass
def iterate_files():
    pass
def stuff_to_output():
    pass
def filter(node: ast.AST) -> bool:
    pass
def filter(node: ast.AST) -> bool:
    pass
def is_dunder(name):
    pass
def to_output(
    fp: TextIO,
    lines: Iterable[Tuple[str, str]],
    format: Literal["csv", "tsv", "json", "nl"] = "csv",
) -> None:
    pass
