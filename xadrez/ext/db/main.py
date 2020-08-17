from flask import Blueprint, current_app
from flask_sqlalchemy import SQLAlchemy

bp = Blueprint("db", __name__)

db = SQLAlchemy(current_app)


class Board(db.Model):
    __tablename__ = "board"
    id = db.Column("id", db.Integer, primary_key=True)
    key = db.Column("key", db.Integer)


class Movement(db.Model):
    __tablename__ = "movement"
    id = db.Column('id', db.Integer, primery_key=True)
    uci = db.Column('uci', db.Unicode)
    color = db.Column('color', db.Unicode)
    board_id = db.Column(
        "board_id",
        db.Integer,
        db.ForeignKey("board.id")
    )

    board = db.relationship("Board", foreign_keys=board_id)
