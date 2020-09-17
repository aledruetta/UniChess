from flask_cors import CORS
from flask_socketio import SocketIO

cors = CORS()
socketio = SocketIO()


def init_app(app):
    cors.init_app(app)
    socketio.init_app(app, cors_allowed_origins="*")
