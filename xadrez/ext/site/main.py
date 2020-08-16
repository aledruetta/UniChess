from flask import Blueprint, render_template, request, redirect, url_for
from wtforms import Form, StringField, validators

from xadrez.ext.engine import UniBoard

bp = Blueprint("site", __name__)


class MoveForm(Form):
    movement = StringField("movement", [validators.Length(min=4, max=4)])


class PlayForm(Form):
    play = StringField("play")


@bp.route("/", methods=["GET", "POST"])
def index():
    board = UniBoard()
    form = PlayForm(request.form)

    if request.method == "POST":
        board.uni_save(mode="w")
        return redirect(url_for("site.board"))

    return render_template(
        "index.html",
        title="UniChess",
        board=board.uni_render(),
        form=form,
    )


@bp.route("/board", methods=["GET", "POST"])
def board():
    form = MoveForm(request.form)
    board = UniBoard()
    board.uni_load()

    if request.method == "POST" and form.validate():
        board.uni_move(form.movement.data)

    return render_template(
        "board.html",
        title="UniChess Board",
        board=board.uni_render(),
        form=form,
    )
