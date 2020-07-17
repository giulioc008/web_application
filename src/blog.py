import flask
from flask import Blueprint
from src.auth import login_required
from src.database import get_database

blueprint = Blueprint("blog", __name__)

@blueprint.route("/create", methods=["GET", "POST"])
@login_required
def create():
	if flask.request.method == "POST":
		title = flask.request.form["title"]
		body = flask.request.form["body"]
		error = None

		if not title:
			error = "Title is required."

		if error is not None:
			flask.flash(error)
		else:
			database = get_database()

			with database.cursor() as cursor:
				cursor.execute("INSERT INTO `post` (`title`, `body`, `author_id`) VALUES (%(title)s, %(body)s, %(user_id)s);", {
					"title": title,
					"body": body,
					"user_id": flask.g.user["id"]
				})
			database.commit()

			return flask.redirect(flask.url_for("blog.index"))

	return flask.render_template("blog/create.html.jinja")


@blueprint.route("/<int:id>/delete", methods=["POST"])
@login_required
def delete(id: int):
	get_post(id)
	database = get_database()

	with database.cursor() as cursor:
		cursor.execute("DELETE FROM `post` WHERE `id`=%(id)s;", {
			"id": id
		})
	database.commit()

	return flask.redirect(flask.url_for("blog.index"))


def get_post(id: int, check_author: bool = True):
	database = get_database()

	with database.cursor() as cursor:
		cursor.execute("SELECT `post.id`, `title`, `body`, `created`, `author_id`, `username` FROM `post`, `user` WHERE `post.author_id`=`user.id` AND `post.id`=%(id)s;", {
			"id": id
		})
		post = cursor.fetchone()

	if post is None:
		werkzeug.exceptions.abort(404, "Post id {} doesn\"t exist.".format(id))

	if check_author and post["author_id"] != flask.g.user["id"]:
		werkzeug.exceptions.abort(403)

	return post


@blueprint.route("/")
def index():
	database = get_database()

	with database.cursor() as cursor:
		cursor.execute("SELECT `post.id`, `title`, `body`, `created`, `author_id`, `username` FROM `post`, `user` WHERE `post.author_id`=`user.id` ORDER BY `created` DESC;")
		posts = cursor.fetchall()

	return flask.render_template("blog/index.html.jinja", posts=posts)


@blueprint.route("/<int:id>/update", methods=["GET", "POST"])
@login_required
def update(id: int):
	post = get_post(id)

	if flask.request.method == "POST":
		title = flask.request.form["title"]
		body = flask.request.form["body"]
		error = None

		if not title:
			error = "Title is required."

		if error is not None:
			flask.flash(error)
		else:
			database = get_database()

			with database.cursor() as cursor:
				cursor.execute("UPDATE `post` SET `title`=%(title)s, `body`=%(body)s WHERE `id`=%(id)s;", {
					"title": title,
					"body": body,
					"id": id
				})
			database.commit()

			return flask.redirect(flask.url_for("blog.index"))

	return flask.render_template("blog/update.html.jinja", post=post)
