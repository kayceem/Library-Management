from typing import List
from database import get_db
from sqlalchemy.orm import Session
import schemas, models, utils
from fastapi import Depends, status, HTTPException, APIRouter

router = APIRouter(prefix="/books", tags=["Books"])


# Get all books
@router.get("/", response_model=List[schemas.BookResponse])
async def get_books(db: Session = Depends(get_db)):
    books = db.query(models.Book).all()
    return books


# Get book with id
@router.get("/{book_id}", response_model=schemas.BookResponse)
async def get_book_by_id(
    book_id: str,
    db: Session = Depends(get_db),
):
    book = utils.check_book(db=db, id=book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    return book


# Regisetr book
@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.BookResponse
)
async def register_book(
    book: schemas.BookBase,
    db: Session = Depends(get_db),
):
    conflicts = utils.check_conflicts_book(db, **book.dict())

    if conflicts:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Duplicate ISBN"
        )
    new_book = models.Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


# Update book detail
@router.post(
    "/detail",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.BookDetailResponse,
)
async def update_book_detail(
    book_detail: schemas.BookDetail,
    db: Session = Depends(get_db),
):
    book = utils.check_book(db=db, id=book_detail.book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    detail = (
        db.query(models.BookDetail)
        .filter(models.BookDetail.book_id == book_detail.book_id)
        .first()
    )

    if detail:
        # Update existing book detail
        for key, value in book_detail.dict().items():
            setattr(detail, key, value)
    else:
        detail = models.BookDetail(**book_detail.dict())
        db.add(detail)
    db.commit()
    db.refresh(detail)
    response = schemas.BookDetailResponse(detail=detail, book=book)
    return response
