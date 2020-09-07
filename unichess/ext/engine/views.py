from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from flask_login import current_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length

from .control import UniBoard

bp = Blueprint("engine", __name__)


class MoveForm(FlaskForm):
    movement = StringField(
        "Movement", validators=[InputRequired(), Length(min=4, max=4)]
    )


class ModalForm(FlaskForm):
    random_id = StringField("Random ID")
    submit = StringField("Submit")
    cancel = StringField("Cancel")


@bp.route("/board/create", methods=["GET", "POST"])
@login_required
def create():

    move_form = MoveForm()
    modal_form = ModalForm()

    uniboard = UniBoard()

    if request.method == "GET":
        uniboard.create()
        session["random_id"] = uniboard.random_id

    elif request.method == "POST":
        session["modal"] = False

        if modal_form.validate_on_submit():
            uniboard.load(session["random_id"])

            if modal_form.cancel.data:
                uniboard.delete()
                return redirect(url_for("site.index"))

            elif modal_form.submit.data:
                return redirect(url_for("engine.play"))

    return render_template(
        "board.html",
        title="UniChess Board",
        board={"svg": UniBoard.render_base(), "id": session["random_id"]},
        move_form=move_form,
        modal_form=modal_form,
        modal=session["modal"],
        auth=session.get("auth", None),
    )


@bp.route("/board/join", methods=["GET", "POST"])
@login_required
def join():

    move_form = MoveForm()
    modal_form = ModalForm()

    if request.method == "POST":
        session["modal"] = False

        if modal_form.validate_on_submit():
            if modal_form.cancel.data:
                return redirect(url_for("site.index"))

            elif random_id := modal_form.random_id.data:
                uniboard = UniBoard()
                uniboard.load(random_id)

                if uniboard.random_id:
                    session["random_id"] = uniboard.random_id
                    uniboard.add_guest(current_user.id)
                    return redirect(url_for("engine.play"))

    return render_template(
        "board.html",
        title="UniChess Board",
        board={"svg": UniBoard.render_base(), "id": None},
        move_form=move_form,
        modal_form=modal_form,
        modal=session["modal"],
        auth=session.get("auth", None),
    )


@bp.route("/board/play", methods=["GET", "POST"])
@login_required
def play():

    move_form = MoveForm()

    uniboard = UniBoard()
    uniboard.load(session["random_id"])

    if request.method == "POST":
        if move_form.validate_on_submit():
            uci = move_form.movement.data
            uniboard.move(uci)

    return render_template(
        "board.html",
        title="UniChess Board",
        board={"svg": uniboard.render(), "id": None},
        move_form=move_form,
        modal_form=None,
        modal=None,
        auth=session.get("auth", None),
    )
