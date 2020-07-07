from app.models import *
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class CVESchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CVE


class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product


class VendorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Vendor


class CPESchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CPE


class ReferenceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Reference


cve_schema = CVESchema()
cves_schema = CVESchema(many=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

vendor_schema = VendorSchema()
vendors_schema = VendorSchema(many=True)

cpe_schema = CPESchema()
cpes_schema = CVESchema(many=True)

reference_schema = ReferenceSchema()
references_schema = ReferenceSchema(many=True)
