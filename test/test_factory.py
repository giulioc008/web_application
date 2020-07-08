import src


def test_config():
	assert not src.create_app().testing
	assert src.create_app({
		"TESTING": True
	}).testing


def test_hello(client):
	response = client.get("/hello")
	assert response.data == b"Hello, World!"
