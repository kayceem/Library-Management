import models
from sqlalchemy.orm import Session

# Check if user exists
def check_user(db: Session, id: str):
    user = db.query(models.User).filter(models.User.user_id == id).first()
    return user


# Check for conflicts in user details
def check_conflicts(db: Session, email: str = None, **kwargs):
    existing_user = (
        db.query(models.User)
        .filter(
            models.User.email == email,
        )
        .first()
    )
    return existing_user

# Check if book exists
def check_book(db: Session, id: str):
    book = db.query(models.Book).filter(models.Book.book_id == id).first()
    return book

# Check for conflicts in book details
def check_conflicts_book(db: Session, isbn: str = None, **kwargs):
    existing_book = (
        db.query(models.Book)
        .filter(
            models.Book.isbn == isbn,
        )
        .first()
    )
    return existing_book

# Check for borrow status of a book
def check_borrowed_book(db: Session, book_id: str = None):
    borrowed_book = (
        db.query(models.BorrowedBook)
        .filter(
            models.BorrowedBook.book_id == book_id,
        )
        .first()
    )
    return borrowed_book
