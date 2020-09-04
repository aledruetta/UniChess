import click

from unichess.ext.db import db

from .models import User

# TODO: usar biblioteca tabulate para apresentação de dados


def createdb():
    """Create databases"""

    db.create_all()

    click.echo("Database created...")


def dropdb():
    """Drop databases"""

    db.drop_all()

    click.echo("Database droped...")


# @click.option("--admin", "-a", required=True, is_flag=True, default=False)
# def createuser(email, passwd, is_admin):


@click.option("--email", "-e", required=True)
@click.option("--passwd", "-p", required=True)
def createadmin(email, passwd):
    """Create admin user"""

    User.create(username="admin", email=email, password=passwd, is_admin=True)

    click.echo("User admin created...")
