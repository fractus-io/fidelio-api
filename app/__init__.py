from flask import Flask
from app.config import TestingConfig, DevelopmentConfig, ProductionConfig
import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy()

from app.api.routes import api
from app.errors.handlers import errors

app.register_blueprint(api)
app.register_blueprint(errors)


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig if str(os.environ.get(
        "PRODUCTION")).lower() == 'true' else DevelopmentConfig)

    db.init_app(app)

    from app.api.routes import api
    from app.errors.handlers import errors

    app.register_blueprint(api)
    app.register_blueprint(errors)

    return app
