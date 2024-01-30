from typing import List
from database import get_db
from sqlalchemy.orm import Session
import schemas, models, utils
from fastapi import Depends, status, HTTPException, APIRouter

router = APIRouter(prefix="/borrow", tags=["Books"])


# Get all borrowed books
@router.get("/", response_model=List[schemas.BookResponse])
async def get_borrowed_books(db: Session = Depends(get_db)):
    borrowed_books = db.query(models.BorrowedBook).all()
    books = [borrowed_book.book for borrowed_book in borrowed_books]
    return books


# Borrow a book
@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.BookBorrow
)
async def borrow_book(
    borrow_details: schemas.BookBorrow,
    db: Session = Depends(get_db),
):
    book = utils.check_book(db=db, id=borrow_details.book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    user = utils.check_user(db=db, id=borrow_details.user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not registered"
        )
    is_borrowed = utils.check_borrowed_book(db=db, book_id=borrow_details.book_id)
    if is_borrowed:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not available"
        )

    borrowed_book = models.BorrowedBook(**borrow_details.dict())
    db.add(borrowed_book)
    db.commit()
    db.refresh(borrowed_book)
    return borrowed_book


# Return a book
@router.put("/", status_code=status.HTTP_201_CREATED, response_model=schemas.BookBorrow)
async def return_book(
    return_details: schemas.BookReturn,
    db: Session = Depends(get_db),
):
    borrowed_book = (
        db.query(models.BorrowedBook)
        .filter(models.BorrowedBook.book_id == return_details.book_id)
        .first()
    )
    if not borrowed_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not borrowed"
        )

    setattr(borrowed_book, "return_date", return_details.return_date)
    db.commit()
    db.refresh(borrowed_book)
    return borrowed_book
