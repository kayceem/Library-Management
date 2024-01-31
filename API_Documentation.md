# API Documentation

## Books

### List All Books

-   **Endpoint:** `/api/books`
-   **Method:** `GET`
-   **Description:** Get a list of all books in the library.
    **Response:**

    ```json
    [
        {
            "title": "string",
            "isbn": 0,
            "published_date": "2024-01-31",
            "genre": "string",
            "book_id": 0
        }
    ]
    ```

### Add a New Book

-   **Endpoint:** `/api/books`
-   **Method:** `POST`
-   **Description:** Add a new book to the library inventory.

    **Request Body:**

    ```json
    {
        "title": "string",
        "isbn": 0,
        "published_date": "2024-01-31",
        "genre": "string"
    }
    ```

    **Response:**

    ```json
    {
        "title": "string",
        "isbn": 0,
        "published_date": "2024-01-31",
        "genre": "string",
        "book_id": 0
    }
    ```

### Get a Book by Id

-   **Endpoint:** `/api/books/{book_id}`
-   **Method:** `GET`
-   **Description:** Get a specific book by its Id.

    **Response:**

    ```json
    {
        "title": "string",
        "isbn": 0,
        "published_date": "2024-01-31",
        "genre": "string",
        "book_id": 0
    }
    ```

### Update Book Details

-   **Endpoint:** `/api/books/detail`
-   **Method:** `POST`
-   **Description:** Update details of a specific book.

    **Request Body:**

    ```json
    {
        "book_id": 0,
        "publisher": "string",
        "language": "string",
        "number_of_pages": 0
    }
    ```

    **Response:**

    ```json
    {
        "detail": {
            "book_id": 0,
            "publisher": "string",
            "language": "string",
            "number_of_pages": 0
        },
        "book": {
            "title": "string",
            "isbn": 0,
            "published_date": "2024-01-31",
            "genre": "string",
            "book_id": 0
        }
    }
    ```

### List All Borrowed Books

-   **Endpoint:** `/api/borrow`
-   **Method:** `GET`
-   **Description:** Get a list of all borrowed books in the library.
    **Response:**

    ```json
    [
        {
            "title": "string",
            "isbn": 0,
            "published_date": "2024-01-31",
            "genre": "string",
            "book_id": 0
        }
    ]
    ```

### Borrow a Book

-   **Endpoint:** `/api/borrow`
-   **Method:** `POST`
-   **Description:** Borrow a book from library inventory.

    **Request Body:**

    ```json
    {
        "user_id": 0,
        "book_id": 0,
        "borrow_date": "2024-01-31"
    }
    ```

    **Response:**

    ```json
    {
        "user_id": 0,
        "book_id": 0,
        "borrow_date": "2024-01-31",
        "return_date": null
    }
    ```

### Return a return

-   **Endpoint:** `/api/return`
-   **Method:** `PUT`
-   **Description:** Return a book to library inventory.
    **Request Body:**

    ```json
    {
        "book_id": 0,
        "return_date": "2024-01-31"
    }
    ```

    **Response:**

    ```json
    {
        "user_id": 0,
        "book_id": 0,
        "borrow_date": "2024-01-31",
        "return_date": "2024-01-31"
    }
    ```

## Users

### List All Members

-   **Endpoint:** `/api/users`
-   **Method:** `GET`
-   **Description:** Get a list of all members of the library.
    **Response:**

    ```json
    [
        {
            "name": "string",
            "email": "user@example.com",
            "user_id": 0,
            "membership_date": "2024-01-31T05:14:49.679Z"
        }
    ]
    ```

### Get a Member by Id

-   **Endpoint:** `/api/users/{user_id}`
-   **Method:** `GET`
-   **Description:** Get a specific member by their Id.

    **Response:**

    ```json
    {
        "name": "string",
        "email": "user@example.com",
        "user_id": 0,
        "membership_date": "2024-01-31T05:14:49.679Z"
    }
    ```

### Add a Member

-   **Endpoint:** `/api/users`
-   **Method:** `POST`
-   **Description:** Add a new member to the library.

    **Request Body:**

    ```json
    {
        "name": "string",
        "email": "user@example.com"
    }
    ```

    **Response:**

    ```json
    {
        "name": "string",
        "email": "user@example.com",
        "user_id": 0,
        "membership_date": "2024-01-31T05:19:01.646Z"
    }
    ```

## Admin

### Add a Admin

-   **Endpoint:** `/api/admin`
-   **Method:** `POST`
-   **Description:** Add a new admin to the library.

    **Request Body:**

    ```json
    {
        "username": "string",
        "password": "stringsts"
    }
    ```

    **Response:**

    ```json
    {
        "username": "string"
    }
    ```

## Login

Authenticate a user by providing a valid username and password.

-   **Endpoint:** `/api/login`
-   **Method:** `POST`
-   **Content-Type:** `application/x-www-form-urlencoded`

**Request Parameters:**

| Parameter | Type   | Description                |
| --------- | ------ | -------------------------- |
| username  | string | User's username (required) |
| password  | string | User's password (required) |

**Request Example:**

```http
Content-Type: application/x-www-form-urlencoded

username=johndoe&password=password
```

**Response:**

A successful login will return a JSON Web Token (JWT) that can be used for authentication in subsequent requests.

```json
{
    "message": "Logged in successfully",
    "data": {
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IktheWMiLCJpYXQiOjE3MDY2Mjk3NDgsImV4cCI6MTcwNjYzMzM0OH0._pbBnzhqp_x7rPMA1b4La9BU_1iNs47kWsEhHkt487E"
    }
}
```
