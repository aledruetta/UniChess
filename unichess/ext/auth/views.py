from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required, logout_user
from wtforms import Form, PasswordField, StringField, validators

from unichess.ext.db import db

from .control import create_user, validate_user

bp = Blueprint("auth", __name__)


class LoginForm(Form):
    email = StringField(
        "email", [validators.length(min=6, max=35), validators.DataRequired()]
    )
    passwd = PasswordField("passwd", [validators.DataRequired()])


class SignupForm(Form):
    username = StringField("username")
    email = StringField(
        "email", [validators.length(min=6, max=35), validators.DataRequired()]
    )
    passwd = PasswordField("passwd", [validators.DataRequired()])


@bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm(request.form)

    if request.method == "POST" and form.validate():
        create_user(form.username.data, form.email.data, form.passwd.data)

        return redirect(url_for("site.index"))
    return render_template("signup.html", title="Sign up", form=form,)


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)

    if request.method == "POST" and form.validate():
        is_user = validate_user(form.email.data, form.passwd.data)
        if is_user:
            return redirect(url_for("site.index"))
    return render_template("login.html", title="Login", form=form,)


@bp.route("/logout", methods=["GET"])
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()

    redirect(url_for("site.index"))
