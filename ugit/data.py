import hashlib
import os
from pathlib import Path

ROOT = Path(".")
GIT_DIR = ROOT / ".ugit"
OBJECTS_DIR = GIT_DIR / "objects"


def init() -> Path:
    # NOTE: makedirs creates directories recursively
    # os.makedirs(GIT_DIR)
    os.makedirs(OBJECTS_DIR)
    return GIT_DIR


def hash_object(path: Path) -> str:
    with open(path, "rb") as input:
        data = input.read()
    # NOTE: use a different/better hashing?
    oid = hashlib.sha1(data).hexdigest()
    with open(OBJECTS_DIR / oid, 'wb') as out:
        out.write(data)
    return oid


def get_object(oid):
    with open(OBJECTS_DIR / oid, 'rb') as f:
        return f.read()
