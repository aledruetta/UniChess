"""Flask extension for database managment commands"""

# import click

# from unichess.ext.db import db
from unichess.ext.db.commands import createdb, dropdb


def init_app(app):

    app.cli.add_command(app.cli.command()(createdb))
    app.cli.add_command(app.cli.command()(dropdb))
