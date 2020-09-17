import click

from unichess.ext.db import db


def createdb():
    """Create databases"""

    db.create_all()
    click.echo("Database created...")


def truncatedb():
    """Truncate data from all tables"""

    meta = db.metadata

    for table in reversed(meta.sorted_tables):
        click.echo(f"Truncando {table} ...")
        db.session.execute(table.delete())

    db.session.commit()


def dropdb():
    """Drop databases"""

    db.drop_all()
    click.echo("Database droped...")
