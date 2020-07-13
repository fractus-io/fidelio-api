from flask import Blueprint, jsonify
from app import db
from app.models import *
from app.schemas import cve_schema, cves_schema, product_schema, products_schema, \
    vendor_schema, vendors_schema, cpe_schema, cpes_schema, reference_schema, \
    references_schema


api = Blueprint('api', __name__)


@api.route("/")
def home():
    cves = CVE.query.all()

    return {
        "cves": cves_schema.dump(cves)
    }


@api.route("/<string:id>")
def cve(id):
    cve = CVE.query.filter_by(id=id).first_or_404()

    return {
        "cve": cve_schema.dump(cve)
    }
