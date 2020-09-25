from .auth import createadmin, createuser, listusers
from .db.commands import createdb, dropdb, truncatedb


def init_app(app):

    app.cli.add_command(app.cli.command()(createdb))
    app.cli.add_command(app.cli.command()(truncatedb))
    app.cli.add_command(app.cli.command()(dropdb))

    app.cli.add_command(app.cli.command()(createadmin))
    app.cli.add_command(app.cli.command()(createuser))
    app.cli.add_command(app.cli.command()(listusers))

    # método alternativo
    # @app.cli.command():
    # def createdb():
    #     pass
