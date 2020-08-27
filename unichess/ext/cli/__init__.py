"""Flask extension for database managment commands"""

from unichess.ext.db.commands import createadmin, createdb, dropdb


def init_app(app):

    app.cli.add_command(app.cli.command()(createdb))
    app.cli.add_command(app.cli.command()(createadmin))
    app.cli.add_command(app.cli.command()(dropdb))

    # método alternativo
    # @app.cli.command():
    # def createdb():
    #     pass
