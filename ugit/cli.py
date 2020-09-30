import sys
from pathlib import Path

import typer

from . import data

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
    print(data.hash_object(name))


@app.command()
def cat_file(oid: str):
    sys.stdout.flush()
    sys.stdout.buffer.write(data.get_object(oid))
