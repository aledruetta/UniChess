from .commands import createadmin, createuser, listusers  # noqa
from .control import login_manager
from .models import User  # noqa
from .views import bp


def init_app(app):
    app.register_blueprint(bp)
    login_manager.init_app(app)
