from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField

from unichess.ext.engine.control import UniBoard

bp = Blueprint("site", __name__)


class PlayForm(FlaskForm):
    play = StringField("play")


@bp.route("/")
def index():
    play_form = PlayForm()

    if request.args.get("play"):

        if current_user.is_authenticated:
            uniboard = UniBoard()

            return redirect(
                url_for("engine.board", random_id=uniboard.random_id)
            )

        return redirect(url_for("auth.signup"))

    # Index rendering on GET
    session["auth"] = session.get("auth", {"is_auth": False, "username": None})

    return render_template(
        "index.html",
        title="UniChess",
        board=UniBoard.render_base(),
        form=play_form,
        auth=session["auth"],
    )
