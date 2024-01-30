from fastapi.testclient import TestClient
from main import app
from fastapi import status

client = TestClient(app)


def test_borrow_book():
    data = {"book_id": 1, "user_id": 1, "borrow_date": "2021-09-01"}
    response = client.post("/api/borrow", json=data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    data = {"book_id": 14, "user_id": 1, "borrow_date": "2021-09-01"}
    response = client.post("/api/borrow", json=data)
    assert response.status_code == status.HTTP_201_CREATED


test_borrow_book()
