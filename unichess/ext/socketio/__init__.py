from flask_cors import CORS
from flask_socketio import SocketIO

cors = CORS()
socketio = SocketIO()


@socketio.on("message")
def handle_message(msg):
    print(msg)


def init_app(app):
    cors.init_app(app)
    socketio.init_app(app, cors_allowed_origins='*')
