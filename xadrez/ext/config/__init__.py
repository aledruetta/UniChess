def init_app(app):
    app.config["SECRET_KEY"] = "abacate01"
    app.config["DEBUG_TB_ENABLED"] = True

    if app.debug:
        app.config["DEBUG_TB_TEMPLATE_EDITOR_ENABLED"] = True
