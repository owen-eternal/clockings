from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(settings='clocking_api.settings.DevConfig'):

    app = Flask(__name__)
    app.config.from_object(settings)

    db.init_app(app)
    migrate.init_app(app, db)

    from .resources import clocking_bp
    app.register_blueprint(clocking_bp)

    return app
