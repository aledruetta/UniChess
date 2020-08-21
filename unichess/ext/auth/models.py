from unichess.ext.db import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.Unicode, unique=True, nullable=False)
    email = db.Column("email", db.Unicode, unique=True, nullable=False)
    passwd = db.Column("passwd", db.Unicode)
    is_admin = db.Column("is_admin", db.Boolean)

    hosts = db.relationship(
        "Board",
        foreign_keys="Board.host_id",
        backref=db.backref("user", lazy=True)
    )

    def __repr__(self):
        return "<User %r>" % self.email
