from app import app
from flask import Blueprint, jsonify
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint


SWAGGER_URL = "/api/docs"
API_URL = "http://localhost:5000/api/spec"

swag = Blueprint('swagger', __name__)


@swag.route("/spec")
def spec():
    return jsonify(swagger(app))


swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name": "Fidelio"
    }
)
