import click
import flask
from flask import Flask
import pymysql


def close_database():
	database = flask.g.pop("database", None)

	if database is not None:
		database.close()


def get_database():
	if "database" not in flask.g:
		flask.g.database = pymysql.connect(
			host="localhost",
			user="webServerUsername",
			password="webServerPassword",
			database="web_application",
			port=3306,
			charset="utf8",
			cursorclass=pymysql.cursors.DictCursor,
			autocommit=False)

	return flask.g.database


def init_app(app: Flask):
	app.teardown_appcontext(close_database)
	app.cli.add_command(init_database_command)


def init_database():
	database = get_database()

	with flask.current_app.open_resource("web_application.sql") as f:
		database.executescript(f.read().decode("utf8"))


@click.command("init-database")
@flask.cli.with_appcontext
def init_database_command():
	init_database()
	click.echo("Initialized the database.")
