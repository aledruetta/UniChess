import click

from unichess.ext.auth.control import create_user
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


@click.option("--email", "-e", required=True)
@click.option("--passwd", "-p", required=True)
def createadmin(email, passwd):
    """Create admin user"""

    create_user(username="admin", email=email, password=passwd, is_admin=True)

    click.echo("User admin created...")
