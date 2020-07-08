import flask
from flask import Flask
from logging import Formatter
from . import auth, blog, database


def create_app(test_config = None):
	app = Flask(__name__, template_folder="templates", static_folder="static")
	app.config.from_mapping({
		"SECRET_KEY": b"\xa3h]\xd5\xc71W\xee\xe0\xd3\xcc4Y\x11 \x7f",
		"DATABASE": os.path.join(app.instance_path, "src.pymysql")
	})
	app.jinja_options = {
		"extensions": [
			"jinja2.ext.do"
			"jinja2.ext.loopcontrols"
		]
	}
	app.jinja_env.trim_blocks=True
	app.jinja_env.lstrip_blocks=True
	flask.logging.default_handler.setFormatter(Formatter(fmt="At %(asctime)s was logged the event:\t%(levelname)s - %(message)s", datefmt="%d/%m/%Y %H:%M:%S"))

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello/")
    def hello():
        return "Hello, World!"

	database.init_app(app)

	app.register_blueprint(auth.blueprint)
	app.register_blueprint(blog.blueprint)

	app.add_url_rule("/", endpoint="index")

	return app