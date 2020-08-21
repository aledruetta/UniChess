from unichess.ext.db import db
from unichess.ext.auth.models import User


def create_user(username, email, passwd, is_admin=False):
    user = User(
        username=username,
        email=email,
        passwd=passwd,
        is_admin=is_admin
    )
    db.session.add(user)
    db.session.commit()
