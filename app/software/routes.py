from flask import Blueprint, jsonify
from app import db
from app.models import *
from app.schemas import cves_schema, product_schema, products_schema, \
    vendor_schema, vendors_schema, cpe_schema, cpes_schema, reference_schema, \
    references_schema


software = Blueprint("software", __name__)


@software.route("/<string:product_name>/<string:version>")
def get_software(product_name, version):
    """
    Get CVEs from CPE with corresponding version and product name
    ---
    tags:
      - CVE
    parameters:
      - name: product_name
        in: path
        required: true
        type: string
        description: name of the CPE product
      - name: version
        in: path
        required: true
        type: string
        description: CPE version
    responses:
      200:
        description: Get corresponding CVEs
      408:
        description: Request timeout
    """
    cves = CVE.query.join(CVE.cpes).filter(
        CPE.version == version
    ).join(Product).filter(
        Product.name == product_name
    ).all()

    return {
        "cves": cves_schema.dump(cves)
    }
