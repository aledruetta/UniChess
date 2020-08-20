import chess
import chess.svg

from unichess.ext.db import db
from unichess.ext.db.models import Board, Movement


class UniBoard(chess.Board):
    def __init__(self, random_id=None, fen=chess.STARTING_FEN):
        super().__init__(fen)
        self.random_id = random_id
        self.db_board_id = None
        self.turn = chess.WHITE

    def db_create_board(self):
        db_board = Board(random_id=self.random_id)
        db.session.add(db_board)
        db.session.commit()

        self.db_board_id = db_board.id

    def db_load_board(self, random_id):
        db_board = Board.query.filter_by(random_id=random_id).first()
        self.db_board_id = db_board.id
        db_movements = Movement.query.filter_by(
            board_id=self.db_board_id
        ).all()
        for movement in db_movements:
            self.uni_move(movement.uci)

    def db_save_movement(self, uci):
        movement = Movement(
            uci=uci, color=self.turn, board_id=self.db_board_id
        )
        db.session.add(movement)
        db.session.commit()

    def uni_render(self):
        return chess.svg.board(board=self)

    def uni_move(self, uci):
        movement = chess.Move.from_uci(uci)
        if movement in self.legal_moves:
            self.push(movement)
