import chess
import chess.svg
from flask import Blueprint, render_template

bp = Blueprint("site", __name__)


def create_board():
    board = chess.Board()
    return chess.svg.board(board=board)


@bp.route("/")
def index():
    return render_template(
        "index.html", title="UniChess", board=create_board(),
    )


@bp.route("/board")
def board():
    return render_template(
        "board.html", title="UniChess Board", board=create_board()
    )
