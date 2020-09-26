from flask import redirect, request, url_for
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, login_required

from .auth import User
from .db import db
from .engine import Board, Movement


class AdminView(ModelView):

    @login_required
    def is_accessible(self):
        if current_user.is_authenticated and current_user.is_admin:
            return True
        return False

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for("auth.login", next=request.url))


admin = Admin(
    name="Dashboard",
    template_mode="bootstrap3",
)
admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(Board, db.session))
admin.add_view(AdminView(Movement, db.session))


def init_app(app):
    admin.init_app(app)
