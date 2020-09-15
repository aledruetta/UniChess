from unichess.ext.db.commands import (
    createdb,
    dropdb,
)

from unichess.ext.auth.commands import (
    createadmin,
    createuser,
    listusers,
)


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
