from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from flask_login import login_required
from flask_wtf import FlaskForm
from wtforms import StringField, validators

from .control import UniBoard

bp = Blueprint("engine", __name__)


class MoveForm(FlaskForm):
    movement = StringField("movement", [validators.Length(min=4, max=4)])


class ModalForm(FlaskForm):
    start = StringField("Start")
    cancel = StringField("Cancel")


@bp.route("/board/<int:random_id>", methods=["GET", "POST"])
@login_required
def board(random_id):
    move_form = MoveForm()
    modal_form = ModalForm()

    uniboard = UniBoard(random_id)
    modal = True

    if request.method == "GET":
        if request.args.get("cancel"):
            return redirect(url_for("site.index"))

        if request.args.get("start"):
            modal = False

    if request.method == "POST" and move_form.validate_on_submit():
        uci = move_form.movement.data
        uniboard.move(uci)
        modal = False

    return render_template(
        "board.html",
        title="UniChess Board",
        board={"svg": uniboard.render(), "id": uniboard.random_id},
        modal=modal,
        move_form=move_form,
        modal_form=modal_form,
        auth=session.get("auth", None),
    )
