from .control import UniBoard  # noqa
from .models import Board, Movement  # noqa
from .views import bp


def init_app(app):
    app.register_blueprint(bp)
