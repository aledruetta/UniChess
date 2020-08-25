from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, validators

from .control import UniBoard

bp = Blueprint("engine", __name__)


class MoveForm(FlaskForm):
    movement = StringField("movement", [validators.Length(min=4, max=4)])


@bp.route("/board/<int:random_id>", methods=["GET", "POST"])
@login_required
def board(random_id):
    form = MoveForm()
    uniboard = UniBoard(random_id)

    auth = {
        "is_auth": current_user.is_authenticated,
        "username": current_user.username
        if current_user.is_authenticated
        else None,
    }

    if request.method == "POST" and form.validate_on_submit():
        uci = form.movement.data
        uniboard.move(uci)

    return render_template(
        "board.html",
        title="UniChess Board",
        board=uniboard.render(),
        form=form,
        auth=auth,
    )
