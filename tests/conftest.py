import os
import tempfile

import pytest

from unichess.app import create_app
from unichess.ext import db


@pytest.fixture
def client():
    app = create_app()
    db_fd, app.config["DATABASE"] = tempfile.mkstemp()
    app.config["TESTING"] = True

    with app.test_client() as client:
        with app.app_context():
            db.init_app(app)
        yield client

    os.close(db_fd)
    os.unlink(app.config["DATABASE"])
