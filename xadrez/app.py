#!/usr/bin/env python3

from flask import Flask

from xadrez.ext import site, toolbar


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "abacate01"
    toolbar.init_app(app)
    site.init_app(app)

    return app
