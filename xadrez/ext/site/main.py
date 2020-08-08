from flask import Blueprint, render_template


bp = Blueprint('site', __name__)


class ChessBoard:
    def __init__(self):
        self.board = []
        self.init_status()

    def init_status(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.board[0] = ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
        self.board[1] = ['♟' for _ in range(8)]
        self.board[-1] = ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
        self.board[-2] = ['♙' for _ in range(8)]

    @property
    def colors(self):
        board = []
        b = 'board-cell-black'
        w = 'board-cell-white'
        for i in range(4):
            board.append(list([b, w] * 4))
            board.append(list([w, b] * 4))

        return board

    def __getitem__(self, i):
        return self.board[i]


@bp.route('/')
def index():
    board = ChessBoard()
    return render_template(
        'index.html',
        title='UniChess',
        cell=board,
        color=board.colors
    )
