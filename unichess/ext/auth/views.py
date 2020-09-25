from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from flask_login import login_required, logout_user
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, EqualTo, InputRequired, Length

from .models import User

bp = Blueprint("auth", __name__)


class LoginForm(FlaskForm):
    email = EmailField(
        "email",
        validators=[
            Length(min=6),
            Email(message="Enter a valid email."),
            InputRequired(),
        ],
    )
    password = PasswordField(
        "password",
        validators=[
            InputRequired(),
            Length(min=6, message="Select a stronger password."),
        ],
    )
    submit = SubmitField("Log In")


class SignupForm(FlaskForm):
    username = StringField("username", [InputRequired()])
    email = EmailField(
        "email",
        validators=[
            Length(min=6),
            Email(message="Enter a valid email."),
            InputRequired(),
        ],
    )
    password = PasswordField(
        "password",
        validators=[
            InputRequired(),
            Length(min=6, message="Select a stronger password."),
        ],
    )
    confirm = PasswordField(
        "Confirm Your Password",
        validators=[
            InputRequired(),
            EqualTo("password", message="Password must much."),
        ],
    )
    submit = SubmitField("Register")


@bp.route("/signup", methods=["GET", "POST"])
def signup():
    signup_form = SignupForm()

    if request.method == "POST" and signup_form.validate_on_submit():

        User.create(
            signup_form.username.data,
            signup_form.email.data,
            signup_form.password.data,
        )

        return redirect(url_for("site.index"))

    return render_template("signup.html", title="Sign up", form=signup_form)


@bp.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()

    if request.method == "POST" and login_form.validate_on_submit():
        if user := User.validate(
            login_form.email.data, login_form.password.data
        ):

            session["auth"] = {
                "is_auth": user.is_authenticated,
                "username": user.username,
            }

            return redirect(url_for("site.index"))

    return render_template("login.html", title="Login", form=login_form)


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    session["auth"] = None

    return redirect(url_for("site.index"))
