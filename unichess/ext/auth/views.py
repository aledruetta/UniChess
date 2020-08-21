from flask import Blueprint, redirect, render_template, request, url_for
from wtforms import Form, PasswordField, StringField, validators

bp = Blueprint("auth", __name__)


class LoginForm(Form):
    email = StringField(
        "email", [validators.length(min=6, max=35), validators.DataRequired()]
    )
    password = PasswordField("password", [validators.DataRequired()])


class SignupForm(Form):
    username = StringField("username")
    email = StringField(
        "email", [validators.length(min=6, max=35), validators.DataRequired()]
    )
    password = PasswordField("password", [validators.DataRequired()])


@bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm(request.form)

    return render_template("signup.html", title="SignUp", form=form,)


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)

    return render_template("login.html", title="Login", form=form,)
