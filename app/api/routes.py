from flask import Blueprint, jsonify
from app import db
from app.models import *


api = Blueprint('api', __name__)


@api.route("/")
def home():
    return {"home": "page"}


@api.route("/<string:variable>")
def greeting(variable):
    return {"hello": variable}
