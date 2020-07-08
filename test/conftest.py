import os
import pytest
import src
import tempfile

with open(os.path.join(os.path.dirname(__file__), "data.sql"), "rb") as f:
	_data_sql = f.read().decode("utf8")


class AuthActions(object):
	def __init__(self, client):
		self._client = client

	def login(self, username = "test", password = "test"):
		return self._client.post("/auth/login", data={
			"username": username,
			"password": password
		})

	def logout(self):
		return self._client.get("/auth/logout")


@pytest.fixture
def auth(client):
	return AuthActions(client)


@pytest.fixture
def app():
	database_fd, database_path = tempfile.mkstemp()

	app = src.create_app({
		"TESTING": True,
		"DATABASE": database_path
	})

	with app.app_context():
		src.database.init_database()
		src.database.get_database().executescript(_data_sql)

	yield app

	os.close(database_fd)
	os.unlink(database_path)


@pytest.fixture
def client(app):
	return app.test_client()


@pytest.fixture
def runner(app):
	return app.test_cli_runner()
