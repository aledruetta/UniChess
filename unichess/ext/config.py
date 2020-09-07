def init_app(app):
    app.config["SECRET_KEY"] = "abacate01"

    # Toolbar
    app.config["DEBUG_TB_ENABLED"] = False
    app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

    # Sqlalchemy
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if app.debug:
        app.config["DEBUG_TB_ENABLED"] = True
        app.config["DEBUG_TB_TEMPLATE_EDITOR_ENABLED"] = True
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
