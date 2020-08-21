from flask import Blueprint, redirect, render_template, request, url_for
from wtforms import Form, StringField, validators

from unichess.ext.engine import UniBoard

bp = Blueprint("site", __name__)


class MoveForm(Form):
    movement = StringField("movement", [validators.Length(min=4, max=4)])


class PlayForm(Form):
    play = StringField("play")


@bp.route("/", methods=["GET", "POST"])
def index():
    form = PlayForm(request.form)

    if request.method == "POST":
        uniboard = UniBoard()
        return redirect(url_for("site.board", random_id=uniboard.random_id))

    return render_template(
        "index.html",
        title="UniChess",
        board=UniBoard.render_base(),
        form=form,
    )


@bp.route("/board/<int:random_id>", methods=["GET", "POST"])
def board(random_id):
    form = MoveForm(request.form)
    uniboard = UniBoard(random_id)

    if request.method == "POST" and form.validate():
        uci = form.movement.data
        uniboard.move(uci)

    return render_template(
        "board.html",
        title="UniChess Board",
        board=uniboard.render(),
        form=form,
    )
