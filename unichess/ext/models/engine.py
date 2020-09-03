from unichess.ext.db import db


class Board(db.Model):
    __tablename__ = "board"

    id = db.Column("id", db.Integer, primary_key=True)
    random_id = db.Column("random_id", db.Integer)

    host_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    movements = db.relationship(
        "Movement", backref=db.backref("board", lazy=True)
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
