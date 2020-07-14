from app import db
from app.models import *
from datetime import datetime
from flask import Blueprint, jsonify
from app.schemas import cve_schema, cves_schema, product_schema, products_schema, \
    vendor_schema, vendors_schema, cpe_schema, cpes_schema, reference_schema, \
    references_schema


cve = Blueprint("cve", __name__)


@cve.route("/")
def all_cves():
    """
    Get all CVEs
    ---
    tags:
      - CVE
    responses:
      200:
        description: Get CVEs
    """
    cves = CVE.query.all()

    return {
        "cves": cves_schema.dump(cves)
    }


@cve.route("/<int:id>")
def cve_by_id(id):
    """
    Get CVE with corresponding id
    ---
    tags:
      - CVE
    parameters:
      - name: id
        in: path
        required: true
        type: integer
        description: ID of the CVE in the database
    responses:
      200:
        description: Get CVEs
      404:
        description: No CVE found
    """
    cve = CVE.query.filter_by(id=id).first_or_404()

    return {
        "cve": cve_schema.dump(cve)
    }


@cve.route("/year")
def cve_last_year():
    """
    Get CVEs from current year
    ---
    tags:
      - CVE
    responses:
      200:
        description: Get CVEs from current year
      408:
        description: Request timeout
    """
    current_time = datetime.now()

    cves = CVE.query.filter(
        current_time.year == db.extract("year", CVE.published_date)
    ).all()

    return {
        "cves": cves_schema.dump(cves)
    }


@cve.route("/month")
def cve_last_month():
    """
    Get CVEs from last month of the year
    ---
    tags:
      - CVE
    responses:
      200:
        description: Get CVEs from last month of the year
      408:
        description: Request timeout
    """
    # FIXME: get rid of hardcoded year
    cves = CVE.query.filter(
        2019 == db.extract("year", CVE.published_date),
        db.extract("month", CVE.published_date) == 12
    ).all()

    return {
        "cves": cves_schema.dump(cves)
    }


@cve.route("/week")
def cve_last_week():
    """
    Get CVEs from last week of the year
    ---
    tags:
      - CVE
    responses:
      200:
        description: Get CVEs from last week of the year
      408:
        description: Request timeout
    """
    # FIXME: get rid of hardcoded year
    cves = CVE.query.filter(
        2019 == db.extract("year", CVE.published_date),
        db.extract("week", CVE.published_date) == 52
    ).all()

    return {
        "cves": cves_schema.dump(cves)
    }


@cve.route("/day")
def cve_last_day():
    """
    Get CVES from last day of the year
    ---
    tags:
      - CVE
    responses:
      200:
        description: Get CVEs from last day of the year
      408:
        description: Request timeout
    """
    # FIXME: get rid of hardcoded year
    cves = CVE.query.filter(
        2019 == db.extract("year", CVE.published_date),
        db.extract("doy", CVE.published_date) == 365
    ).all()

    return {
        "cves": cves_schema.dump(cves)
    }


@cve.route("/latest")
def cve_latest():
    """
    Get 30 latest CVEs
    ---
    tags:
      - CVE
    responses:
      200:
        description: Get CVEs from last day of the year
      408:
        description: Request timeout
    """
    current_time = datetime.now()

    cves = CVE.query.filter(
        current_time.year == db.extract("year", CVE.published_date)
    ).order_by(
        CVE.published_date.desc()
    ).limit(30).all()

    return {
        "cves": cves_schema.dump(cves)
    }


@cve.route("/count/<int:year>")
def cve_count_by_year(year):
    """
    Get CVE count by year
    ---
    tags:
      - CVE
    parameters:
      - name: year
        in: path
        required: true
        type: integer
        description: Year with certain amount of CVEs
    responses:
      200:
        description: Get CVE count
    """
    count = CVE.query.filter(
        year == db.extract("year", CVE.published_date)
    ).count()

    return {
        "cve_count": count
    }


@cve.route("/count/<int:year>/<int:month>")
def cve_count_by_year_month(year, month):
    """
    Get CVE count by year
    ---
    tags:
      - CVE
    parameters:
      - name: year
        in: path
        required: true
        type: integer
        description: Year with certain amount of CVEs
      - name: month
        in: path
        required: true
        type: integer
        description: Month of a year with certain amount of CVEs
    responses:
      200:
        description: Get CVE count
    """
    count = CVE.query.filter(
        year == db.extract("year", CVE.published_date),
        month == db.extract("month", CVE.published_date)
    ).count()

    return {
        "cve_count": count
    }
