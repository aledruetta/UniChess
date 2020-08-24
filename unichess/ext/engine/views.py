from flask import Blueprint, render_template, request
from flask_login import login_required
from wtforms import Form, StringField, validators

from .control import UniBoard

bp = Blueprint("engine", __name__)


class MoveForm(Form):
    movement = StringField("movement", [validators.Length(min=4, max=4)])


class PlayForm(Form):
    play = StringField("play")


@bp.route("/board/<int:random_id>", methods=["GET", "POST"])
@login_required
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
