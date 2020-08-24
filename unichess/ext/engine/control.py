from random import randint

from unichess.ext.db import db
from .models import Board, Movement

import chess
import chess.svg
from flask_login import login_required

MIN_ID = 1
MAX_ID = 2 ** 63


class UniBoard(chess.Board):
    def __init__(self, random_id=None, fen=chess.STARTING_FEN):
        super().__init__(fen)

        self.db_board_id = None
        self.random_id = random_id
        self.turn = chess.WHITE

        if not random_id:
            self.create_board()
        else:
            self.load_board()

    @login_required
    def create_board(self):
        self.random_id = randint(MIN_ID, MAX_ID)

        # TODO: Trocar host_id hardcoded por usuário logado
        db_board = Board(random_id=self.random_id, host_id=1)
        db.session.add(db_board)
        db.session.commit()

        self.db_board_id = db_board.id

    @login_required
    def load_board(self):
        db_board = Board.query.filter_by(random_id=self.random_id).first()
        self.db_board_id = db_board.id
        db_movements = Movement.query.filter_by(
            board_id=self.db_board_id
        ).all()
        for movement in db_movements:
            movement = chess.Move.from_uci(movement.uci)
            self.push(movement)

    @login_required
    def save_movement(self, uci):
        movement = Movement(
            uci=uci, color=self.turn, board_id=self.db_board_id
        )
        db.session.add(movement)
        db.session.commit()

    @login_required
    def move(self, uci):
        movement = chess.Move.from_uci(uci)
        if movement in self.legal_moves:
            self.push(movement)
            self.save_movement(uci)

    @staticmethod
    def render_base():
        return chess.svg.board(chess.BaseBoard())

    @login_required
    def render(self):
        return chess.svg.board(board=self)
