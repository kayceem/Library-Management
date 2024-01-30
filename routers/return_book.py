from database import get_db
from sqlalchemy.orm import Session
import schemas, models
from fastapi import Depends, status, HTTPException, APIRouter

router = APIRouter(prefix="/return", tags=["Books"])


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
            status_code=status.HTTP_400_BAD_REQUEST, detail="Book not borrowed"
        )

    setattr(borrowed_book, "return_date", return_details.return_date)
    db.commit()
    db.refresh(borrowed_book)
    return borrowed_book
