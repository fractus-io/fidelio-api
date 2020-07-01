import os
import click
from app.models import *
from app import create_app, db
from unzip_cve import extract_data_from_zip


# # closing the app
# print("Database added. Exiting the program...")


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


def fill_db():
    # creating app to access database without starting the server
    app = create_app()

    with app.app_context():
        """db_manipulation goes here"""
        cves = extract_data_from_zip("nvd/cve/nvdcve-1.1-2020.json.zip")
        for cve_data in cves:
            cve = CVE(**cve_data)
            db.session.add(cve)
            db.session.commit()


def fill_db_all():
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


funcs = {
    "flush": flush,
    "recreate-tables": flush,
    "create-tables": create_tables,
    "fill-db-latest": fill_db,
    "fill-db-all": fill_db_all,
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
