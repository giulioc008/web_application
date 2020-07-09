import click
import flask
from flask import Flask
from flask.cli import with_appcontext
import pymysql


def close_database(_):
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
		script = f.read().decode("utf8")
		script = script.replace("\n", " ")
		script = script.replace("; ", "\n")
		script = script.splitlines()

		with database.cursor() as cursor:
			for i in script:
				cursor.execute(i)
		database.commit()


@click.command("init-database")
@with_appcontext
def init_database_command():
	init_database()
	click.echo("Initialized the database.")
