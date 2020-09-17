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

from unichess.ext.socket import socketio

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

    form = MoveForm()

    uniboard = UniBoard(session["random_id"])
    user = uniboard.get_user_color()
    turn = uniboard.get_turn_color()
    rival = uniboard.get_rival_color()

    if request.method == "POST" and form.validate_on_submit() and user == turn:
        uci = form.movement.data
        if uniboard.move(uci):
            event = f'{session["random_id"]}_{rival}'
            socketio.emit(event)

    return render_template(
        "board.html",
        title="UniChess Board",
        board={
            "id": uniboard.random_id,
            "username": current_user.username,
            "color": user,
            "svg": uniboard.render(),
        },
        move_form=form,
        modal_form=None,
        modal=None,
        auth=session.get("auth", None),
    )


@bp.route("/board/leave")
@login_required
def leave():

    uniboard = UniBoard(session["random_id"])
    color = uniboard.get_user_color()

    if color == uniboard.WHITE:
        uniboard.destroy()

    event = f'{session["random_id"]}_{color}_leave'
    socketio.emit(event)

    return redirect(url_for("site.index"))
