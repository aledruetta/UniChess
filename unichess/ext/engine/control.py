from random import randint

import chess
import chess.svg
from flask_login import current_user

from unichess.ext.db import db

from .models import Board, Movement


class UniBoard(chess.Board):
    MIN_ID = 1
    MAX_ID = 2 ** 63
    BLACK = "black"
    WHITE = "white"

    def __init__(self, random_id=None):
        super().__init__()

        self.id = None
        self.random_id = random_id

        if not random_id:
            self._create()
        else:
            self._load(random_id)

    def _create(self):
        self.turn = chess.WHITE
        self.random_id = randint(self.MIN_ID, self.MAX_ID)

        db_board = Board(random_id=self.random_id, host_id=current_user.id)
        db.session.add(db_board)
        db.session.commit()

        self.id = db_board.id

    def _load(self, random_id):
        try:
            db_board = Board.query.filter_by(random_id=random_id).first()
            self.id = db_board.id
        except AttributeError as err:
            print(err)
        else:
            self.random_id = random_id
            db_movements = Movement.query.filter_by(board_id=self.id).all()

            for movement in db_movements:
                movement = chess.Move.from_uci(movement.uci)
                self.push(movement)

    def _save(self, uci):
        movement = Movement(uci=uci, color=self.turn, board_id=self.id)

        db.session.add(movement)
        db.session.commit()

    def _get_host_id(self):
        db_board = Board.query.get(self.id)
        return db_board.host_id

    def _get_guest_id(self):
        db_board = Board.query.get(self.id)
        return db_board.guest_id

    def destroy(self, random_id=None):
        if not random_id:
            random_id = self.random_id

        board = Board.query.filter_by(random_id=random_id).first()
        db.session.delete(board)
        db.session.commit()

    def add_guest(self, guest_id):
        db_board = Board.query.get(self.id)
        db_board.guest_id = guest_id
        db.session.commit()

    def get_user_color(self):
        if current_user.id == self._get_host_id():
            return self.WHITE
        return self.BLACK

    def get_rival_color(self):
        if current_user.id == self._get_host_id():
            return self.BLACK
        return self.WHITE

    def get_turn_color(self):
        return self.WHITE if self.turn else self.BLACK

    def move(self, uci):
        movement = chess.Move.from_uci(uci)

        if movement in self.legal_moves:
            self.push(movement)
            self._save(uci)
            return True
        return False

    def render(self):
        return chess.svg.board(self)

    @staticmethod
    def render_base():
        return chess.svg.board(chess.BaseBoard())
