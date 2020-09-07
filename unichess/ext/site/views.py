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

from unichess.ext.engine import UniBoard

bp = Blueprint("site", __name__)


class PlayForm(FlaskForm):
    create_game = StringField("Create Game")
    join_game = StringField("Join Game")


@bp.route("/")
def index():
    session["modal"] = True
    play_form = PlayForm()

    if request.args.get("create_game"):
        if current_user.is_authenticated:
            return redirect(url_for("engine.create"))

        return redirect(url_for("auth.signup"))

    if request.args.get("join_game"):
        if current_user.is_authenticated:
            return redirect(url_for("engine.join"))

        return redirect(url_for("auth.signup"))

    return render_template(
        "index.html",
        title="UniChess",
        board=UniBoard.render_base(),
        form=play_form,
        auth=session.get("auth", None),
    )
