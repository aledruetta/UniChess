from datetime import datetime, time

from unichess.ext.db import db


class Board(db.Model):
    __tablename__ = "board"

    id = db.Column("id", db.Integer, primary_key=True)
    random_id = db.Column("random_id", db.Integer)
    created_at = db.Column(
        "created_at", db.DateTime, default=datetime.now, nullable=False
    )

    host_id = db.Column(
        "host_id",
        db.Integer,
        db.ForeignKey("user.id"),
        unique=True,
        nullable=False,
    )
    host_time = db.Column(
        "host_time", db.Time, default=time(0, 0), nullable=False
    )
    guest_id = db.Column("guest_id", db.Integer, db.ForeignKey("user.id"))
    guest_time = db.Column(
        "guest_time", db.Time, default=time(0, 0), nullable=False
    )

    movements = db.relationship(
        "Movement",
        cascade="all, delete, delete-orphan",
        backref="board",
        lazy=True,
    )

    def __repr__(self):
        return "<Board %r>" % self.movements


class Movement(db.Model):
    __tablename__ = "movement"

    id = db.Column("id", db.Integer, primary_key=True)
    uci = db.Column("uci", db.Unicode, nullable=False)
    color = db.Column("color", db.Boolean, nullable=False)

    board_id = db.Column(db.Integer, db.ForeignKey("board.id"), nullable=False)

    def __repr__(self):
        return "<Movement %r>" % self.uci
