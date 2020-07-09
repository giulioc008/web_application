import functools
import flask
from flask import Blueprint
from src.database import get_database

blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@blueprint.before_app_request
def load_logged_in_user():
	user_id = flask.session.get("user_id")

	if user_id is None:
		flask.g.user = None
	else:
		database = get_database()

		with database.cursor() as cursor:
			cursor.execute("SELECT * FROM `user` WHERE `id`=%(user_id)s;", {
				"user_id": user_id
			})
			flask.g.user = cursor.fetchone()


@blueprint.route("/login", methods=["GET", "POST"])
def login():
	if flask.request.method == "POST":
		username = flask.request.form["username"]
		password = flask.request.form["password"]
		database = get_database()
		error = None

		with database.cursor() as cursor:
			cursor.execute("SELECT * FROM `user` WHERE `username`=%(username)s;", {
				"username": username
			})
			user = cursor.fetchone()

		if user is None:
			error = "Incorrect username."
		elif not werkzeug.security.check_password_hash(user["password"], password):
			error = "Incorrect password."

		if error is None:
			flask.session.clear()
			flask.session["user_id"] = user["id"]
			return flask.redirect(flask.url_for("index"))

		flask.flash(error)

	return flask.render_template("auth/login.html.jinja")


def login_required(view):
	@functools.wraps(view)
	def wrapped_view(**kwargs):
		if flask.g.user is None:
			return flask.redirect(flask.url_for("auth.login"))

		return view(**kwargs)

	return wrapped_view


@blueprint.route("/logout")
def logout():
	flask.session.clear()
	return flask.redirect(flask.url_for("index"))


@blueprint.route("/register", methods=["GET", "POST"])
def register():
	if flask.request.method == "POST":
		username = flask.request.form["username"]
		password = flask.request.form["password"]
		database = get_database()
		error = None

		with database.cursor() as cursor:
			cursor.execute("SELECT `id` FROM `user` WHERE `username`=%(username)s;", {
				"username": username
			})
			user = cursor.fetchone()

		if not username:
			error = "Username is required."
		elif not password:
			error = "Password is required."
		elif user is not None:
			error = "User {} is already registered.".format(username)

		if error is None:
			with database.cursor() as cursor:
				cursor.execute("INSERT INTO user (username, password) VALUES (%(username)s, %(password)s);", {
					"username": username,
					"password": werkzeug.security.generate_password_hash(password)
				})
			database.commit()
			return flask.redirect(flask.url_for("auth.login"))

		flask.flash(error)

	return flask.render_template("auth/register.html.jinja")
