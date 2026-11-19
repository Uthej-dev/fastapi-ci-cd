
from fastapi.testclient import TestClient
from test import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI"}


def test_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert "users" in response.json()

def get_games():
    response = client.get("/games")
    assert response.status_code == 200
    assert "games" in response.json()