import sys
from pathlib import Path

import typer

from . import data, base

app = typer.Typer()


@app.command()
def init():
    try:
        path = data.init()
        typer.echo(f"Initialized empty ugit repository in {path}")
    except FileExistsError:
        typer.echo("ugit has been initialized already")


@app.command()
def hash_object(name: Path):
    with open(name, 'rb') as f:
        print(data.hash_object(f.read()))


@app.command()
def cat_file(oid: str):
    sys.stdout.flush()
    sys.stdout.buffer.write(data.get_object(oid, expected=None))


@app.command()
def write_tree():
    print(base.write_tree())
