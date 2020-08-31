from flask_login import LoginManager

from unichess.ext.auth import models

login_manager = LoginManager()


@login_manager.user_loader
def user_loader(user_id):
    return models.User.query.get(user_id)
