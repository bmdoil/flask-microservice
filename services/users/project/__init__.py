# services/users/project/__init__.py

import os
from flask import Flask  # , jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS

db = SQLAlchemy()
toolbar = DebugToolbarExtension()
cors = CORS()


def create_app(script_info=None):
    # instantiate app
    app = Flask(__name__)

    # set config

    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    toolbar.init_app(app)
    cors.init_app(app)
    
    # register blueprints
    from project.api.users import users_blueprint

    app.register_blueprint(users_blueprint)

    # shell context for flask cli
    @app.shell_context_processor  # used to register the app and db to the shell
    def ctx():
        return {"app": app, "db": db}

    return app
