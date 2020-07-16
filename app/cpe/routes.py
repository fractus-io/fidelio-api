from flask import Blueprint, jsonify
from app import db
from app.models import *
from app.schemas import cves_schema, product_schema, products_schema, \
    vendor_schema, vendors_schema, cpe_schema, cpes_schema, reference_schema, \
    references_schema


cpe = Blueprint("cpe", __name__)


@cpe.route("/")
def all_cpes():
    """
    Get all CPEs
    ---
    tags:
      - CPE
    responses:
      200:
        description: Get CPEs
    """
    cpes = CPE.query.all()

    return {
        "cpes": cpes_schema.dump(cpes)
    }


@cpe.route("/<string:id>")
def cpe_by_id(id):
    """
    Get CPE with corresponding id
    ---
    tags:
      - CPE
    parameters:
      - name: id
        in: path
        required: true
        type: integer
        description: ID of the CPE in the database
    responses:
      200:
        description: Get CPEs
      404:
        description: No CPE found
    """
    cpe = CPE.query.filter_by(id=id).first_or_404()

    return {
        "cpe": cpe_schema.dump(cpe)
    }


@cpe.route("/product/<string:product_name>")
def cpe_by_product(product_name):
    """
    Get CPE with corresponding product name
    ---
    tags:
      - CPE
    parameters:
      - name: product_name
        in: path
        required: true
        type: string
        description: Product name of the CPE in the database
    responses:
      200:
        description: Get CPEs with corresponding product name
    """
    cpes = CPE.query.join(Product).filter(
        Product.name == product_name
    ).all()

    return {
        "cpes": cpes_schema.dump(cpes)
    }


@cpe.route("/vendor/<string:vendor_name>")
def cpe_by_vendor(vendor_name):
    """
    Get CPE with corresponding vendor name
    ---
    tags:
      - CPE
    parameters:
      - name: vendor_name
        in: path
        required: true
        type: string
        description: Vendor name of the CPE in the database
    responses:
      200:
        description: Get CPEs with corresponding vendor name
    """
    cpes = CPE.query.join(Vendor).filter(
        Vendor.name == vendor_name
    ).all()

    return {
        "cpes": cpes_schema.dump(cpes)
    }
