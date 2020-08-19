from unichess.ext.db import db


def create_db():
    db.create_all()


def drop_db():
    db.drop_all()


# def populate_deb():
#     pass
