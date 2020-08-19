def init_app(app):
    app.config["SECRET_KEY"] = "abacate01"
    app.config["DEBUG_TB_ENABLED"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

    if app.debug:
        app.config["DEBUG_TB_TEMPLATE_EDITOR_ENABLED"] = True
