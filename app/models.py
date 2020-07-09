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
    cvss_base = db.Column(db.Float(precision=1))
    cvss_impact = db.Column(db.Float(precision=1))
    cvss_exploit = db.Column(db.Float(precision=1))
    cvss_access_vector = db.Column(db.String(20))
    cvss_access_complexity = db.Column(db.String(20))
    cvss_access_authentication = db.Column(db.String(20))
    cvss_confidentiality_impact = db.Column(db.String(20))
    cvss_integrity_impact = db.Column(db.String(20))
    cvss_availability_impact = db.Column(db.String(20))
    cvss_vector = db.Column(db.Text)

    # many to many relationship
    cpes = db.relationship("CPE", secondary="software", backref="cves")

    def __repr__(self):
        return f"<CVE[{self.id},{self.cve_id}]>"


# -------------------------------------------------------------------------------------


class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    cpes = db.relationship("CPE", backref="vendor", lazy=True)

    def __repr__(self):
        return f"<Vendor[{self.id},{self.name}]>"


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    cpes = db.relationship("CPE", backref="product", lazy=True)

    def __repr__(self):
        return f"<Product[{self.id},{self.name}]>"


class CPE(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    part = db.Column(db.String(1), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    version = db.Column(db.String(255), nullable=False)
    update_version = db.Column(db.String(255))
    edition = db.Column(db.String(255))
    lang = db.Column(db.String(20))
    sw_edition = db.Column(db.String(255))
    target_sw = db.Column(db.String(255))
    target_hw = db.Column(db.String(255))
    other = db.Column(db.String(255))

    references = db.relationship("Reference", backref="CPE", lazy=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey("vendor.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)

    def __repr__(self):
        return f"<CPE[{self.id},{self.title}]>"


class Reference(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cpe_id = db.Column(db.Integer, db.ForeignKey("CPE.id"), nullable=False)
    url = db.Column(db.Text)
    type = db.Column(db.String(255))
    desc = db.Column(db.String(255))

    def __repr__(self):
        return f"<Reference[{self.id},{self.type},{self.desc}]>"


# -------------------------------------------------------------------------------------


software = db.Table(
    "software",
    db.Column("cve_id", db.Integer, db.ForeignKey("CVE.id")),
    db.Column("cpe_id", db.Integer, db.ForeignKey("CPE.id")),
)
