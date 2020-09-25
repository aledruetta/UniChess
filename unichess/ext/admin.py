from flask_admin import Admin

admin = Admin(name="UniChess Admin", template_mode="bootstrap3")


def init_app(app):
    admin.init_app(app)
