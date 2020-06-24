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


@api.route("/add")
def time():
    # pass
    t = Test()
    db.session.add(t)
    db.session.commit()

    return {"nice": 200}


@api.route("/get")
def get():
    tests = Test.query.first()
    return {"t": tests.id}
