from app import db
from datetime import datetime


class CVE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cve_id = db.Column(db.String(20), nullable=False)
    cwe_id = db.Column(db.String(15), nullable=False)
    published_date = db.Column(db.DateTime, nullable=False)
    last_modified_date = db.Column(db.DateTime, nullable=False)
    summary = db.Column(db.Text, nullable=False)
    # impact based columns
    cvss_base = db.Column(db.Float(precision=1), nullable=True)
    cvss_impact = db.Column(db.Float(precision=1), nullable=True)
    cvss_exploit = db.Column(db.Float(precision=1), nullable=True)
    cvss_access_vector = db.Column(db.String(20), nullable=True)
    cvss_access_complexity = db.Column(db.String(20), nullable=True)
    cvss_access_authentication = db.Column(db.String(20), nullable=True)
    cvss_confidentiality_impact = db.Column(db.String(20), nullable=True)
    cvss_integrity_impact = db.Column(db.String(20), nullable=True)
    cvss_availability_impact = db.Column(db.String(20), nullable=True)
    cvss_vector = db.Column = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<CVE[{self.id},{self.cve_id}]>"
