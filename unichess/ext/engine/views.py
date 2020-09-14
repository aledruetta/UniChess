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

from unichess.ext.socketio import socketio

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

    if request.method == "POST" and modal_form.validate_on_submit():
        session["modal"] = False

        if modal_form.cancel.data:
            UniBoard(session["random_id"]).destroy()
            session["random_id"] = None
            return redirect(url_for("site.index"))

        return redirect(url_for("engine.play"))

    elif request.method == "GET":
        uniboard = UniBoard()
        session["random_id"] = uniboard.random_id

    return render_template(
        "board.html",
        title="UniChess Board",
        board={"svg": UniBoard.render_base(), "id": uniboard.random_id},
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

    if request.method == "POST" and modal_form.validate_on_submit():

        if modal_form.cancel.data:
            session["modal"] = False
            return redirect(url_for("site.index"))

        else:
            uniboard = UniBoard(modal_form.random_id.data)

            if uniboard.random_id:
                session["modal"] = False
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

    uniboard = UniBoard(session["random_id"])

    if request.method == "POST":
        if move_form.validate_on_submit():
            uci = move_form.movement.data
            uniboard.move(uci)

            event = str(session["random_id"])
            data = {"id": event}
            print(event, data)
            socketio.emit(event, data)

    return render_template(
        "board.html",
        title="UniChess Board",
        board={
            "id": uniboard.random_id,
            "username": current_user.username,
            "color": uniboard.get_color(),
            "svg": uniboard.render(),
        },
        move_form=move_form,
        modal_form=None,
        modal=None,
        auth=session.get("auth", None),
    )
