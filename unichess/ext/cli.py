from unichess.ext.auth import createadmin, createuser, listusers
from unichess.ext.db.commands import createdb, dropdb


def init_app(app):

    app.cli.add_command(app.cli.command()(createdb))
    app.cli.add_command(app.cli.command()(createadmin))
    app.cli.add_command(app.cli.command()(createuser))
    app.cli.add_command(app.cli.command()(listusers))
    app.cli.add_command(app.cli.command()(dropdb))

    # método alternativo
    # @app.cli.command():
    # def createdb():
    #     pass
