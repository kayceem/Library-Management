from fastapi.testclient import TestClient
from main import app
from fastapi import status

client = TestClient(app)


def test_get_users():
    response = client.get("/api/users/")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)


def test_get_user_by_id():
    response = client.get("/api/users/1")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), dict)


def test_create_user():
    data = {
        "name": "Name good",
        "email": "unique@email.com",
    }
    response = client.post("/api/users/", json=data)
    assert response.status_code == status.HTTP_201_CREATED
    assert isinstance(response.json(), dict)


test_get_users()
test_get_user_by_id()
test_create_user()