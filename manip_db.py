import os
import click
from app.models import *
from app import create_app, db
from unzip_cpe import parse_xml
from unzip_cve import extract_data_from_zip


def flush():
    # creating app to access database without starting the server
    app = create_app()

    with app.app_context():
        """db_manipulation goes here"""
        db.drop_all()
        db.create_all()


def create_tables():
    # creating app to access database without starting the server
    app = create_app()

    with app.app_context():
        """db_manipulation goes here"""
        db.create_all()


def fill_cve():
    # creating app to access database without starting the server
    app = create_app()

    with app.app_context():
        """db_manipulation goes here"""
        for file in [f for f in os.listdir("nvd/cve") if not f.startswith(".")]:
            cves = extract_data_from_zip(f"nvd/cve/{file}")
            for cve_data in cves:
                cve = CVE(**cve_data)
                db.session.add(cve)
                db.session.commit()


def fill_cpe():
    # creating app to access database without starting the server
    app = create_app()

    with app.app_context():
        """db_manipulation goes here"""
        xml_data = parse_xml("nvd/cpe/test.xml.zip")
        cpes = xml_data["cpes"]
        vendors = xml_data["vendors"]
        products = xml_data["products"]

        for vendor_name in vendors:
            vendor = Vendor(name=vendor_name)
            db.session.add(vendor)
            db.session.commit()

        for product_name in products:
            product = Product(name=product_name)
            db.session.add(product)
            db.session.commit()

        for cpe_data in cpes:
            cpe_data_raw = {k: v for k, v in cpe_data.items() if k not in ["vendor", "product", "references"]}

            cpe = CPE(**cpe_data_raw)

            vendor = Vendor.query.filter_by(name=cpe_data["vendor"]["name"]).first()
            product = Product.query.filter_by(name=cpe_data["product"]["name"]).first()

            if vendor is None:
                print("no vendor found")
                continue
            if product is None:
                print("no product found")
                continue

            cpe.vendor = vendor
            cpe.product = product

            db.session.add(cpe)
            db.session.commit()

            for ref_data in cpe_data["references"]:
                reference = Reference(**ref_data)
                reference.CPE = cpe
                db.session.add(reference)
                db.session.commit()


funcs = {
    "flush": flush,
    "recreate-tables": flush,
    "create-tables": create_tables,
    "fill-db-cve": fill_cve,
    "fill-db-cpe": fill_cpe,
}


@click.command()
@click.argument("action")
def manip(action):
    """Database manipulation tool"""
    try:
        funcs[action].__call__()
    except KeyError:
        ctx = click.get_current_context()
        click.echo(f"Action {action} not found", err=True)
        click.echo(ctx.get_help())
        ctx.exit()


if __name__ == "__main__":
    manip()
