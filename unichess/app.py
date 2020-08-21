#!/usr/bin/env python3

from flask import Flask

from unichess.ext import auth, cli, config, db, site, toolbar


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    toolbar.init_app(app)
    cli.init_app(app)
    auth.init_app(app)
    site.init_app(app)

    return app
