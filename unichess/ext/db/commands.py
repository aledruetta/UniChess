import click
from tabulate import tabulate

from unichess.ext.auth import User
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


# @click.option("--admin", "-a", required=True, is_flag=True, default=False)
# def createuser(email, passwd, is_admin):


@click.option("--email", "-e", required=True)
@click.option("--passwd", "-p", required=True)
def createadmin(email, passwd):
    """Create admin user"""

    User.create(username="admin", email=email, password=passwd, is_admin=True)
    click.echo("User admin successfully created...")


@click.option("--username", "-u", required=True)
@click.option("--email", "-e", required=True)
@click.option("--passwd", "-p", required=True)
def createuser(username, email, passwd):
    """Create normal user"""

    user = User.create(
        username=username, email=email, password=passwd, is_admin=False
    )
    click.echo(f"User <{user.username}, {user.email}> successfully created...")


def listusers():
    """List users from database"""

    users = User.query.order_by(User.email).all()
    click.echo(tabulate([
        [u.username, u.email, "admin" if u.is_admin else None]
        for u in users
    ]))
