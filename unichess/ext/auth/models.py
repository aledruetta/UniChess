from werkzeug.security import check_password_hash, generate_password_hash

from unichess.ext.db import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.Unicode, unique=True, nullable=False)
    email = db.Column("email", db.Unicode, unique=True, nullable=False)
    passwd = db.Column("passwd", db.Unicode)
    is_admin = db.Column("is_admin", db.Boolean)
    authenticated = db.Column(db.Boolean, default=False)

    hosts = db.relationship(
        "Board",
        foreign_keys="Board.host_id",
        backref=db.backref("user", lazy=True),
    )

    def set_passwd(self, passwd):
        self.passwd = generate_password_hash(passwd)

    def check_passwd(self, passwd):
        return check_password_hash(self.passwd, passwd)

    def is_active(self):
        return True

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

    def __repr__(self):
        return "<User %r>" % self.email
