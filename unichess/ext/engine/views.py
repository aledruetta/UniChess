from flask import Blueprint, render_template, request, session
from flask_login import login_required
from flask_wtf import FlaskForm
from wtforms import StringField, validators

from .control import UniBoard

bp = Blueprint("engine", __name__)


class MoveForm(FlaskForm):
    movement = StringField("movement", [validators.Length(min=4, max=4)])


@bp.route("/board/<int:random_id>", methods=["GET", "POST"])
@login_required
def board(random_id):

    move_form = MoveForm()
    uniboard = UniBoard(random_id)

    if request.method == "POST" and move_form.validate_on_submit():
        uci = move_form.movement.data
        uniboard.move(uci)

    return render_template(
        "board.html",
        title="UniChess Board",
        board=uniboard.render(),
        form=move_form,
        auth=session.get("auth", None),
    )
