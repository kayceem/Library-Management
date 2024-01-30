from fastapi.testclient import TestClient
from main import app
from fastapi import status

client = TestClient(app)


def test_return_book():
    data = {"book_id": 1, "return_date": "2021-09-01"}
    response = client.put("/api/return", json=data)
    assert response.status_code == status.HTTP_201_CREATED


test_return_book()
