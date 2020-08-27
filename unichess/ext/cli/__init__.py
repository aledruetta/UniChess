"""Flask extension for database managment commands"""

import click

from unichess.ext.db import db


def init_app(app):

    # TODO: usera biblioteca tabulate

    @app.cli.command()
    def createdb():
        """Create a brand new database"""
        db.create_all()
        click.echo("Database created!")

    @app.cli.command()
    def dropdb():
        """Drop all databases"""
        db.drop_all()
        click.echo("Database droped!")
