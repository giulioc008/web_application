import pymysql
import pytest
import src


def test_get_close_database(app):
	with app.app_context():
		database = src.database.get_database()
		assert database is src.database.get_database()

	with pytest.raises(sqlite3.ProgrammingError) as e:
		database.execute("SELECT 1;")

		assert "closed" in str(e.value)


def test_init_database_command(runner, monkeypatch):
	class Recorder(object):
		called = False

	def fake_init_database():
		Recorder.called = True

	monkeypatch.setattr("src.database.init_database", fake_init_database)
	result = runner.invoke(args=[
		"init-database"
	])
	assert "Initialized" in result.output
	assert Recorder.called
