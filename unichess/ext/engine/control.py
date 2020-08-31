from random import randint

import chess
import chess.svg
from flask_login import current_user

from unichess.ext.db import db
from unichess.ext.engine import models

MIN_ID = 1
MAX_ID = 2 ** 63


class UniBoard(chess.Board):
    def __init__(self, random_id=None, fen=chess.STARTING_FEN):
        super().__init__(fen)

        self.db_board_id = None
        self.random_id = random_id
        self.turn = chess.WHITE

        if not random_id:
            self.create()
        else:
            self.load()

    def create(self):
        self.random_id = randint(MIN_ID, MAX_ID)

        db_board = models.Board(
            random_id=self.random_id, host_id=current_user.id
        )
        db.session.add(db_board)
        db.session.commit()

        self.db_board_id = db_board.id

    def load(self):
        db_board = models.Board.query.filter_by(
            random_id=self.random_id
        ).first()
        self.db_board_id = db_board.id
        db_movements = models.Movement.query.filter_by(
            board_id=self.db_board_id
        ).all()
        for movement in db_movements:
            movement = chess.Move.from_uci(movement.uci)
            self.push(movement)

    def delete(self):
        models.Board.query.filter_by(random_id=self.random_id).delete()
        db.session.commit()

    def add_guest(self, guest_id):
        db_board = models.Board.query.get(self.db_board_id)
        db_board.guest_id = guest_id
        db.session.commit()

    def save(self, uci):
        movement = models.Movement(
            uci=uci, color=self.turn, board_id=self.db_board_id
        )
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
