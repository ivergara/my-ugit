import hashlib
import os
from pathlib import Path
from enum import Enum, auto

ROOT = Path(".")
GIT_DIR = ROOT / ".ugit"
OBJECTS_DIR = GIT_DIR / "objects"


class ObjectType(Enum):
    BLOB = auto()
    TREE = auto()


def init() -> Path:
    # NOTE: makedirs creates directories recursively
    # os.makedirs(GIT_DIR)
    os.makedirs(OBJECTS_DIR)
    return GIT_DIR


def hash_object(data: bytes, type_: ObjectType = ObjectType.BLOB) -> str:
    # NOTE: use a different/better hashing?
    obj = type_.name.encode() + b'\x00' + data
    oid = hashlib.sha1(obj).hexdigest()
    with open(OBJECTS_DIR / oid, 'wb') as out:
        out.write(obj)
    return oid


def get_object(oid, expected=ObjectType.BLOB):
    with open(OBJECTS_DIR / oid, 'rb') as f:
        obj = f.read()

    type_, _, content = obj.partition(b'\x00')
    type_ = type_.decode()

    if expected is not None and type_ != expected.value:
        raise ValueError(f'Expected {expected}, got {type_}')
    return content
