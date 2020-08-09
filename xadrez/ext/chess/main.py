import chess
import chess.svg


def create_board():
    board = chess.Board()
    return chess.svg.board(board=board)
