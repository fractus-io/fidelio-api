import click
from app.models import *
from app import create_app, db


# # closing the app
# print("Database added. Exiting the program...")


def flush():
    # creating app to access databse without starting the server
    app = create_app()

    with app.app_context():
        """db_manipulation goes here"""
        db.drop_all()
        db.create_all()


def create_tables():
    # creating app to access databse without starting the server
    app = create_app()

    with app.app_context():
        """db_manipulation goes here"""
        db.create_all()


funcs = {
    "flush": flush,
    "recreate-tables": flush,
    "create-tables": create_tables
    # TODO: fill the db
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
