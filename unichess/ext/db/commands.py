import click
from sqlalchemy.exc import OperationalError

from unichess.ext.db import db


def createdb():
    """Create databases"""

    db.create_all()
    click.echo("Database created...")


def truncatedb():
    """Truncate data from all tables"""

    meta = db.metadata

    try:
        for table in reversed(meta.sorted_tables):
            click.echo(f"Truncando {table} ...")
            db.session.execute(table.delete())
    except OperationalError:
        click.echo("Você tentou truncar tabelas inexistentes... ")
    else:
        db.session.commit()


def dropdb():
    """Drop databases"""

    db.drop_all()
    click.echo("Database droped...")
