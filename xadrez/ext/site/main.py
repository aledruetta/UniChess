import chess
import chess.svg
from flask import Blueprint, render_template, request
from wtforms import Form, StringField, validators

bp = Blueprint("site", __name__)


class MoveForm(Form):
    movement = StringField("movement", [validators.Length(min=2, max=4)])


def save_board(board, mode="a"):
    with open("jogo.txt", mode) as fd:
        fd.write(board.fen() + "\n")


def load_board():
    with open("jogo.txt") as fd:
        lines = fd.readlines()

    return lines[-1]


def create_board():
    board = chess.Board()
    save_board(board, "w")

    return board


def render_board(board):
    return chess.svg.board(board=board)


@bp.route("/")
def index():
    board = create_board()
    return render_template(
        "index.html", title="UniChess", board=render_board(board),
    )


@bp.route("/board", methods=["GET", "POST"])
def board():
    form = MoveForm(request.form)
    board = chess.Board(load_board())

    if request.method == "POST" and form.validate():
        m = chess.Move.from_uci(form.movement.data)
        board.push(m)
        save_board(board)

    return render_template(
        "board.html",
        title="UniChess Board",
        board=render_board(board),
        form=form,
    )
