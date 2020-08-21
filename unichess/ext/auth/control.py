from unichess.ext.db import db
from unichess.ext.auth.models import User


def create_user(username, email, passwd, admin=False):
    user = User(
        username=username,
        email=email,
        passwd=passwd,
        admin=admin
    )
    db.session.add(user)
    db.session.commit()
