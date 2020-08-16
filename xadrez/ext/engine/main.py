import chess
import chess.svg


def save_board(board, mode="a"):
    with open("jogo.txt", mode) as fd:
        fd.write(board.fen() + "\n")


def create_board():
    board = chess.Board()
    save_board(board, "w")

    return board


def load_board():
    try:
        with open("jogo.txt") as fd:
            lines = fd.readlines()
            if len(lines) > 0:
                return chess.Board(lines[-1])
    except FileNotFoundError:
        return create_board()


def render_board(board):
    return chess.svg.board(board=board)


def move_piece(uci):
    return chess.Move.from_uci(uci)
