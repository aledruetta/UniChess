from flask_login import LoginManager

from unichess.ext.db.models import User

login_manager = LoginManager()


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)
