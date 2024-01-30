import models
from sqlalchemy.orm import Session


def check_user(db: Session, id: str):
    user = db.query(models.User).filter(models.User.user_id == id).first()
    return user


def check_conflicts(db: Session, email: str = None, **kwargs):
    existing_user = (
        db.query(models.User)
        .filter(
            models.User.email == email,
        )
        .first()
    )
    return existing_user


def check_book(db: Session, id: str):
    book = db.query(models.Book).filter(models.Book.book_id == id).first()
    return book


def check_conflicts_book(db: Session, isbn: str = None, **kwargs):
    existing_book = (
        db.query(models.Book)
        .filter(
            models.Book.isbn == isbn,
        )
        .first()
    )
    return existing_book


def check_borrowed_book(db: Session, book_id: str = None):
    borrowed_book = (
        db.query(models.BorrowedBook)
        .filter(
            models.BorrowedBook.book_id == book_id,
        )
        .first()
    )
    return borrowed_book
