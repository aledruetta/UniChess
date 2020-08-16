from flask import Blueprint, render_template, request
from wtforms import Form, StringField, validators

from xadrez.ext.engine import UniBoard

bp = Blueprint("site", __name__)


class MoveForm(Form):
    movement = StringField("movement", [validators.Length(min=2, max=4)])


@bp.route("/")
def index():
    board = UniBoard()

    return render_template(
        "index.html", title="UniChess", board=board.uni_render(),
    )


@bp.route("/board", methods=["GET", "POST"])
def board():
    form = MoveForm(request.form)
    board = UniBoard()
    board.uni_load()

    if request.method == "POST" and form.validate():
        board.uni_move(form.movement.data)
        board.uni_save()

    return render_template(
        "board.html",
        title="UniChess Board",
        board=board.uni_render(),
        form=form,
    )
