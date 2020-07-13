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

from app.cve.routes import cve
from app.cpe.routes import cpe
from app.errors.handlers import errors
from app.docs.routes import swag, swaggerui_blueprint, SWAGGER_URL

app.register_blueprint(cve, url_prefix="/api/cve")
app.register_blueprint(cpe, url_prefix="/api/cpe")
app.register_blueprint(errors)
app.register_blueprint(swag)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig if str(os.environ.get(
        "PRODUCTION")).lower() == 'true' else DevelopmentConfig)

    db.init_app(app)
    ma.init_app(app)

    from app.cve.routes import cve
    from app.cpe.routes import cpe
    from app.errors.handlers import errors
    from app.docs.routes import swag, swaggerui_blueprint, SWAGGER_URL

    profiler.init_app(app)

    app.register_blueprint(cve, url_prefix="/api/cve")
    app.register_blueprint(cpe, url_prefix="/api/cpe")
    app.register_blueprint(errors)
    app.register_blueprint(swag, url_prefix="/api")
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app
