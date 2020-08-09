#!/usr/bin/env python3

from flask import Flask

from xadrez.ext import chess, site


def create_app():
    app = Flask(__name__)
    chess.init_app(app)
    site.init_app(app)

    return app
