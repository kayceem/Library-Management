from fastapi.testclient import TestClient
from main import app
from fastapi import status

client = TestClient(app)


def test_get_books():
    response = client.get("/api/books/")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), list)


def test_get_book_by_id():
    response = client.get("/api/books/1")
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.json(), dict)


def test_register_book():
    data = {
        "title": "Test Book",
        "isbn": "7894567451245",
        "published_date": "2022-01-01",
        "genre": "Test Genre",
    }
    response = client.post("/api/books/", json=data)
    assert response.status_code == status.HTTP_201_CREATED
    assert isinstance(response.json(), dict)


def test_update_book_detail():
    data = {
        "book_id": "1",
        "publisher": "Publsiher",
        "language": "English",
        "number_of_pages": 100,
    }
    response = client.post("/api/books/detail", json=data)
    # print(response.json())
    assert response.status_code == status.HTTP_201_CREATED


test_get_books()
test_get_book_by_id()
# test_register_book()
test_update_book_detail()
