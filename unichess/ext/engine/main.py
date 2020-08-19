import chess
import chess.svg

from unichess.ext.db.models import Board, Movement
from unichess.ext.db import db


class UniBoard(chess.Board):
    def __init__(self, random_id=None, fen=chess.STARTING_FEN):
        super().__init__(fen)
        self.random_id = random_id
        self.db_board = None

    def db_create_board(self):
        db_board = Board(random_id=self.random_id)
        db.session.add(db_board)
        db.session.commit()

        self.db_board = db_board

    def db_load_board(self, random_id):
        self.db_board = Board.query.filter_by(random_id=random_id).first()

    def db_save_movement(self, uci, color):
        movement = Movement(uci=uci, color=color, board_id=self.db_board.id)
        db.session.add(movement)
        db.session.commit()

    def uni_render(self):
        return chess.svg.board(board=self)

    def uni_move(self, uci):
        movement = chess.Move.from_uci(uci)
        if movement in self.legal_moves:
            self.push(movement)
            self.db_save_movement(uci, self.turn)
