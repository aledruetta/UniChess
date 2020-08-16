from random import randint

from flask import Blueprint, redirect, render_template, request, url_for
from wtforms import Form, StringField, validators

from xadrez.ext.engine import UniBoard

bp = Blueprint("site", __name__)

MIN_ID = 1
MAX_ID = 2 ** 64


class MoveForm(Form):
    movement = StringField("movement", [validators.Length(min=4, max=4)])


class PlayForm(Form):
    play = StringField("play")


@bp.route("/", methods=["GET", "POST"])
def index():
    board = UniBoard(None)
    form = PlayForm(request.form)

    if request.method == "POST":
        board.uni_save(mode="w")
        board_id = randint(MIN_ID, MAX_ID)

        return redirect(url_for("site.board", board_id=board_id))

    return render_template(
        "index.html", title="UniChess", board=board.uni_render(), form=form,
    )


@bp.route("/board/<int:board_id>", methods=["GET", "POST"])
def board(board_id):
    form = MoveForm(request.form)
    board = UniBoard(board_id)
    board.uni_load()

    if request.method == "POST" and form.validate():
        board.uni_move(form.movement.data)

    return render_template(
        "board.html",
        title="UniChess Board",
        board=board.uni_render(),
        form=form,
    )
