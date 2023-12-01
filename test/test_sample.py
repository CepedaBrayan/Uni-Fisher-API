from .setup import client


def test_sample():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
