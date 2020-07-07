from flask import Blueprint, jsonify
from app import db
from app.models import *
from app.schemas import cve_schema, cves_schema


api = Blueprint('api', __name__)


@api.route("/")
def home():
    cve = CVE.query.first()

    return {"home": cve_schema.dump(cve)}


@api.route("/<string:variable>")
def greeting(variable):
    return {"hello": variable}
