from app.models import *
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class CVESchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CVE
        include_relationships = True


class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        include_relationships = True


class VendorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Vendor
        include_relationships = True


class CPESchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CPE
        # include_fk = True
        include_relationships = True


class ReferenceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Reference
        # include_fk = True
        include_relationships = True


cve_schema = CVESchema()
cves_schema = CVESchema(many=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

vendor_schema = VendorSchema()
vendors_schema = VendorSchema(many=True)

cpe_schema = CPESchema()
cpes_schema = CPESchema(many=True)

reference_schema = ReferenceSchema()
references_schema = ReferenceSchema(many=True)
