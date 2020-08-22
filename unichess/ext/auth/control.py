from flask_login import LoginManager, login_user
from werkzeug.security import generate_password_hash

from unichess.ext.auth.models import User
from unichess.ext.db import db

login_manager = LoginManager()


def create_user(username, email, passwd, is_admin=False):
    hash_passwd = generate_password_hash(passwd)
    user = User(
        username=username, email=email, passwd=hash_passwd, is_admin=is_admin
    )
    db.session.add(user)
    db.session.commit()


def validate_user(email, passwd):
    user = User.query.filter_by(email=email).first()
    if user and user.check_passwd(passwd):
        user.authenticated = True
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)

        return True
    return False


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)
