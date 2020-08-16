from flask import Blueprint, render_template, request
from wtforms import Form, StringField, validators

from xadrez.ext.engine import (
    create_board,
    load_board,
    move_piece,
    render_board,
    save_board,
)

bp = Blueprint("site", __name__)


class MoveForm(Form):
    movement = StringField("movement", [validators.Length(min=2, max=4)])


@bp.route("/")
def index():
    board = create_board()

    return render_template(
        "index.html", title="UniChess", board=render_board(board),
    )


@bp.route("/board", methods=["GET", "POST"])
def board():
    form = MoveForm(request.form)
    board = load_board()

    if request.method == "POST" and form.validate():
        m = move_piece(form.movement.data)
        board.push(m)
        save_board(board)

    return render_template(
        "board.html",
        title="UniChess Board",
        board=render_board(board),
        form=form,
    )
