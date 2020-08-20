from flask import Blueprint, redirect, render_template, request, url_for
from wtforms import Form, StringField, validators, PasswordField

from unichess.ext.engine import UniBoard

bp = Blueprint("site", __name__)


class MoveForm(Form):
    movement = StringField("movement", [validators.Length(min=4, max=4)])


class PlayForm(Form):
    play = StringField("play")


class LoginForm(Form):
    email = StringField("email", [
        validators.length(min=6, max=35),
        validators.DataRequired()
    ])
    password = PasswordField("password", [validators.DataRequired()])


class SignupForm(Form):
    username = StringField("username")
    email = StringField("email", [
        validators.length(min=6, max=35),
        validators.DataRequired()
    ])
    password = PasswordField("password", [validators.DataRequired()])


@bp.route("/", methods=["GET", "POST"])
def index():
    form = PlayForm(request.form)

    if request.method == "POST":
        uniboard = UniBoard()
        return redirect(url_for("site.board", random_id=uniboard.random_id))

    return render_template(
        "index.html",
        title="UniChess",
        board=UniBoard.render_base(),
        form=form,
    )


@bp.route("/board/<int:random_id>", methods=["GET", "POST"])
def board(random_id):
    form = MoveForm(request.form)
    uniboard = UniBoard(random_id)

    if request.method == "POST" and form.validate():
        uci = form.movement.data
        uniboard.move(uci)

    return render_template(
        "board.html",
        title="UniChess Board",
        board=uniboard.render(),
        form=form,
    )


@bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm(request.form)

    return render_template(
        "signup.html",
        title="SignUp",
        form=form,
    )


@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)

    return render_template(
        "login.html",
        title="Login",
        form=form,
    )
