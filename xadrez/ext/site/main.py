from flask import Blueprint, render_template


bp = Blueprint('site', __name__)


def start_position():
    cell = [[' ' for _ in range(8)] for _ in range(8)]
    cell[0] = ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
    cell[1] = ['♟' for _ in range(8)]
    cell[-1] = ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
    cell[-2] = ['♙' for _ in range(8)]

    return cell


def colors():
    lst = []
    inc = 0
    for i in range(8):
        lst.append([])
        for j in range(8):
            if (i * 8 + j + inc) % 2 == 0:
                color = 'board-cell-black'
            else:
                color = 'board-cell-white'
            lst[i].append(color)
        inc += 1

    return lst


@bp.route('/')
def index():
    return render_template(
        'index.html',
        title='UniChess',
        cell=start_position(),
        color=colors(),
    )
