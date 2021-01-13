from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(settings='clocking_api.settings.DevConfig'):

    app = Flask(__name__)
    app.config.from_object(settings)

    from .colections.resources import clocking_bp
    app.register_blueprint(clocking_bp)

    return app
