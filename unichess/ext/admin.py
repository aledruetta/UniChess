from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from .auth import User
from .db import db
from .engine import Board, Movement

admin = Admin(name="UniChess Admin", template_mode="bootstrap3")
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Board, db.session))
admin.add_view(ModelView(Movement, db.session))


def init_app(app):
    admin.init_app(app)
