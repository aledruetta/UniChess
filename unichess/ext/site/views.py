from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField

from unichess.ext.auth.views import SignupForm
from unichess.ext.engine.control import UniBoard

bp = Blueprint("site", __name__)


class PlayForm(FlaskForm):
    play = StringField("play")


@bp.route("/", methods=["GET", "POST"])
def index():
    form = PlayForm()

    if request.method == "POST" and form.validate_on_submit():
        if current_user and current_user.is_authenticated:
            uniboard = UniBoard()
            return redirect(
                url_for("engine.board", random_id=uniboard.random_id)
            )

        form = SignupForm(request.form)
        return render_template("signup.html", title="Sign up", form=form,)

    return render_template(
        "index.html",
        title="UniChess",
        board=UniBoard.render_base(),
        form=form,
    )
