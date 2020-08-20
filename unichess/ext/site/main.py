from random import randint

from flask import Blueprint, redirect, render_template, request, url_for
from wtforms import Form, StringField, validators

from unichess.ext.engine import UniBoard

bp = Blueprint("site", __name__)

MIN_ID = 1
MAX_ID = 2 ** 63


class MoveForm(Form):
    movement = StringField("movement", [validators.Length(min=4, max=4)])


class PlayForm(Form):
    play = StringField("play")


@bp.route("/", methods=["GET", "POST"])
def index():
    form = PlayForm(request.form)

    if request.method == "POST":
        random_id = randint(MIN_ID, MAX_ID)
        uniboard = UniBoard(random_id)
        uniboard.db_create_board()

        return redirect(url_for("site.board", random_id=random_id))

    return render_template(
        "index.html", title="UniChess", board="", form=form,
    )


@bp.route("/board/<int:random_id>", methods=["GET", "POST"])
def board(random_id):
    form = MoveForm(request.form)
    uniboard = UniBoard()
    uniboard.db_load_board(random_id)

    if request.method == "POST" and form.validate():
        uci = form.movement.data
        uniboard.uni_move(uci)
        uniboard.db_save_movement(uci)

    return render_template(
        "board.html",
        title="UniChess Board",
        board=uniboard.uni_render(),
        form=form,
    )
