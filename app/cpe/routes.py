from flask import Blueprint, jsonify
from app import db
from app.models import *
from app.schemas import cpe_schema, cves_schema, product_schema, products_schema, \
    vendor_schema, vendors_schema, cpe_schema, cpes_schema, reference_schema, \
    references_schema


cpe = Blueprint("cpe", __name__)


@cpe.route("/")
def all_cpes():
    cpes = CVE.query.all()

    return {
        "cpes": cpes_schema.dump(cpes)
    }


@cpe.route("/<string:id>")
def cpe_by_id(id):
    cpe = CPE.query.filter_by(id=id).first_or_404()

    return {
        "cpe": cpe_schema.dump(cpe)
    }
