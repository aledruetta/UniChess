#!/usr/bin/env python3

from flask import Flask

from xadrez.ext import site


def create_app():
    app = Flask(__name__)
    site.init_app(app)

    return app
