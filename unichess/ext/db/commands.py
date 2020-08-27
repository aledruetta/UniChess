import click

from unichess.ext.db import db

# TODO: usar biblioteca tabulate para apresentação de dados


def createdb():
    """Create databases"""

    db.create_all()
    click.echo("Database created...")


def dropdb():
    """Drop databases"""

    db.drop_all()
    click.echo("Database droped...")


# def populate_deb():
#     pass
