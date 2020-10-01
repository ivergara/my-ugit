from pathlib import Path

from . import data
from .data import ObjectType


def write_tree(directory: Path = Path('.')):
    if not directory.is_dir():
        raise ValueError(f"The given path '{directory}' is not a directory.")

    entries = []

    for entry in directory.iterdir():
        if is_ignored(entry):
            continue

        if entry.is_file() and not entry.is_symlink():
            with open(entry, 'rb') as f:
                oid = data.hash_object(f.read())
            entries.append((entry.name, oid, ObjectType.BLOB))

        elif entry.is_dir() and not entry.is_symlink():
            oid = write_tree(entry)
            entries.append((entry.name, oid, ObjectType.TREE))

    tree = ''.join(f'{type_} {oid} {name}\n'
                   for name, oid, type_
                   in sorted(entries))

    return data.hash_object(tree.encode(), ObjectType.TREE)


def is_ignored(path: Path) -> bool:
    return '.ugit' in path.parts
