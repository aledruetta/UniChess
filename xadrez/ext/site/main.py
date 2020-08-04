from flask import Blueprint, render_template


bp = Blueprint('site', __name__)


@bp.route('/')
def index():
    cell = [['.' for _ in range(8)] for _ in range(8)]

    return render_template(
        'index.html',
        title='UniChess',
        cell=cell,
    )
