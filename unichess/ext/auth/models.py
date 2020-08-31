from flask_login import UserMixin, login_user
from werkzeug.security import check_password_hash, generate_password_hash

from unichess.ext.db import db


class User(UserMixin, db.Model):
    __tablename__ = "user"

    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.Unicode, unique=True, nullable=False)
    email = db.Column("email", db.Unicode, unique=True, nullable=False)
    password = db.Column("password", db.Unicode)
    is_admin = db.Column("is_admin", db.Boolean, default=False)
    authenticated = db.Column(db.Boolean, default=False)

    hosts = db.relationship(
        "Board",
        foreign_keys="Board.host_id",
        backref=db.backref("user", lazy=True),
    )

    def set_password(self, password):
        self.password = generate_password_hash(password, method="sha256")

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @classmethod
    def create(cls, username, email, password, is_admin=False):
        user = cls(
            username=username, email=email, password=None, is_admin=is_admin
        )
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

    @classmethod
    def validate(cls, email, password):
        user = cls.query.filter_by(email=email).first()
        if user.check_password(password):
            user.authenticated = True
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)

            return user
        return None

    # def is_active(self):
    #     return True

    # def get_id(self):
    #     return self.id

    # def is_authenticated(self):
    #     return self.authenticated

    # def is_anonymous(self):
    #     return False

    def __repr__(self):
        return "<User %r>" % self.email
