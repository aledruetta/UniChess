from .control import login_manager
from .views import bp


def init_app(app):
    login_manager.init_app(app)
    app.register_blueprint(bp)
