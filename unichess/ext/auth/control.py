from flask_login import LoginManager, login_user

from unichess.ext.auth.models import User
from unichess.ext.db import db

login_manager = LoginManager()


def create_user(username, email, password, is_admin=False):
    user = User(
        username=username, email=email, password=None, is_admin=is_admin
    )
    user.set_password(password)
    db.session.add(user)
    db.session.commit()


def validate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        user.authenticated = True
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)

        return user
    return None


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)
