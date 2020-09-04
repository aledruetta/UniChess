from random import randint

import chess
import chess.svg
from flask_login import current_user

from unichess.ext.db import db

from .models import Board, Movement

MIN_ID = 1
MAX_ID = 2 ** 63


class UniBoard(chess.Board):
    def __init__(self, fen=chess.STARTING_FEN):
        super().__init__(fen)

        self._id = None
        self.random_id = None
        self.turn = chess.WHITE

    def create(self):
        self.random_id = randint(MIN_ID, MAX_ID)

        db_board = Board(random_id=self.random_id, host_id=current_user.id)
        db.session.add(db_board)
        db.session.commit()

        self._id = db_board.id

    def load(self, random_id):
        self.random_id = random_id
        db_board = Board.query.filter_by(random_id=self.random_id).first()
        self._id = db_board.id

        db_movements = Movement.query.filter_by(board_id=self._id).all()

        for movement in db_movements:
            movement = chess.Move.from_uci(movement.uci)
            self.push(movement)

    def delete(self):
        Board.query.filter_by(random_id=self.random_id).delete()
        db.session.commit()

    def add_guest(self, guest_id):
        db_board = Board.query.get(self._id)
        db_board.guest_id = guest_id
        db.session.commit()

    def save(self, uci):
        movement = Movement(uci=uci, color=self.turn, board_id=self._id)

        db.session.add(movement)
        db.session.commit()

    def move(self, uci):
        movement = chess.Move.from_uci(uci)

        if movement in self.legal_moves:
            self.push(movement)
            self.save(uci)

    @staticmethod
    def render_base():
        return chess.svg.board(chess.BaseBoard())

    def render(self):
        return chess.svg.board(board=self)
