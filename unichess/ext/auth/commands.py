import click
from tabulate import tabulate

from .models import User


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
    click.echo(
        tabulate(
            [
                [u.username, u.email, "admin" if u.is_admin else None]
                for u in users
            ]
        )
    )
