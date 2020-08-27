from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required, logout_user
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from .control import create_user, validate_user

bp = Blueprint("auth", __name__)


class LoginForm(FlaskForm):
    email = EmailField(
        "email",
        validators=[
            Length(min=6),
            Email(message="Enter a valid email."),
            DataRequired(),
        ],
    )
    password = PasswordField(
        "password",
        validators=[
            DataRequired(),
            Length(min=6, message="Select a stronger password."),
        ],
    )
    submit = SubmitField("Log In")


class SignupForm(FlaskForm):
    username = StringField("username", [DataRequired()])
    email = EmailField(
        "email",
        validators=[
            Length(min=6),
            Email(message="Enter a valid email."),
            DataRequired(),
        ],
    )
    password = PasswordField(
        "password",
        validators=[
            DataRequired(),
            Length(min=6, message="Select a stronger password."),
        ],
    )
    confirm = PasswordField(
        "Confirm Your Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Password must much."),
        ],
    )
    submit = SubmitField("Register")


@bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()

    # print(request.method)
    # if form.validate():
    #     print("Validate!")
    # if form.is_submitted:
    #     print("Is submitted!")
    # if form.validate_on_submit():
    #     print("Validate on submit!")
    # print(form.errors)

    if request.method == "POST" and form.validate_on_submit():
        create_user(form.username.data, form.email.data, form.password.data)

        return redirect(url_for("site.index"))

    return render_template(
        "signup.html", title="Sign up", form=form, auth=None
    )


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if request.method == "POST" and form.validate_on_submit():
        is_user = validate_user(form.email.data, form.password.data)
        if is_user:
            return redirect(url_for("site.index"))

    return render_template("login.html", title="Login", form=form, auth=None)


@bp.route("/logout")
@login_required
def logout():
    logout_user()

    return redirect(url_for("site.index"))
