#!/usr/bin/env python3

from flask import Flask

from unichess.ext import (
    admin,
    auth,
    cli,
    config,
    db,
    engine,
    site,
    socket,
    toolbar,
)


def create_app():
    app = Flask(__name__)

    config.init_app(app)
    db.init_app(app)
    auth.init_app(app)
    admin.init_app(app)
    cli.init_app(app)
    engine.init_app(app)
    site.init_app(app)
    socket.init_app(app)
    toolbar.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app()
    socket.socketio.run(app, debug=True)
