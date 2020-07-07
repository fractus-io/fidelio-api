import os
from flask import Flask
from flask_profiler import Profiler
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from app.config import TestingConfig, DevelopmentConfig, ProductionConfig


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy()
profiler = Profiler()
ma = Marshmallow()

from app.api.routes import api
from app.errors.handlers import errors

app.register_blueprint(api)
app.register_blueprint(errors)


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig if str(os.environ.get(
        "PRODUCTION")).lower() == 'true' else DevelopmentConfig)

    db.init_app(app)
    ma.init_app(app)

    from app.api.routes import api
    from app.errors.handlers import errors

    profiler.init_app(app)

    app.register_blueprint(api)
    app.register_blueprint(errors)

    return app
