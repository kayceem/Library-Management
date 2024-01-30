from pydantic import BaseModel, EmailStr, Field, validator
from datetime import datetime, date


class UserBase(BaseModel):
    name: str = Field(min_length=4, max_length=25)
    email: EmailStr

    class Config:
        orm_mode = True


class UserResponse(UserBase):
    user_id: int
    membership_date: datetime


class BookBase(BaseModel):
    title: str = Field(min_length=3, max_length=255)
    isbn: int
    published_date: date
    genre: str = Field(min_length=3, max_length=255)

    @validator("isbn")
    def validate_isbn(cls, v):
        if len(str(v)) != 13:
            raise ValueError("ISBN must be exactly 13 digits")
        return v

    class Config:
        orm_mode = True


class BookResponse(BookBase):
    book_id: int


class BookDetail(BaseModel):
    book_id: int
    publisher: str = Field(min_length=3, max_length=255)
    language: str = Field(min_length=3, max_length=255)
    number_of_pages: int

    @validator("book_id")
    def validate_book_id(cls, v):
        if v <= 0:
            raise ValueError("Book ID must be greater than 0")
        return v

    class Config:
        orm_mode = True


class BookDetailResponse(BaseModel):
    detail: BookDetail
    book: BookResponse


class BookBorrow(BaseModel):
    user_id: int
    book_id: int
    borrow_date: date

    class Config:
        orm_mode = True


class BookReturn(BaseModel):
    book_id: int
    return_date: date

    class Config:
        orm_mode = True


class BorrowedBook(BaseModel):
    title: str

    class Config:
        orm_mode = True
