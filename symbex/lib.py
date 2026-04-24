import fnmatch
import ast
from ast import literal_eval, parse, AST, AsyncFunctionDef, FunctionDef, ClassDef
import codecs
from dataclasses import dataclass
from itertools import zip_longest
from pathlib import Path
import re
import textwrap
from typing import Iterable, List, Optional, Tuple


def find_symbol_nodes(
    code: str, filename: str, symbols: Iterable[str]
) -> List[Tuple[AST, Optional[str]]]:
    "Returns ast Nodes matching symbols"
    pass


def code_for_node(
    code: str, node: AST, class_name: str, signatures: bool, docstrings: bool
) -> Tuple[str, int]:
    "Returns the code for a given node"
    pass


def add_docstring(definition: str, node: AST, docstrings: bool, is_method: bool) -> str:
    pass


def match(name: str, symbols: Iterable[str]) -> bool:
    "Returns True if name matches any of the symbols, resolving wildcards"
    pass


def function_definition(function_node: AST):
    pass


def class_definition(class_def):
    # Base classes
    pass


def annotation_definition(annotation: AST) -> str:
    pass


def read_file(path):
    pass


@dataclass
class TypeSummary:
    fully: bool
    partially: bool


def type_summary(node: AST) -> Optional[TypeSummary]:
    pass


def quoted_string(s):
    pass


def import_line_for_function(
    function_name: str, filepath: str, possible_root_dirs: List[str]
) -> str:
    """
    Returns eg 'from foo.bar import baz' if filepath is /Users/dev/foo/bar.py
    and function_name is baz and possible_root_dirs is a list that contains
    /Users/dev
    """
    pass
