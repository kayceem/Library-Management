from pydantic import BaseModel, EmailStr, Field
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

    class Config:
        orm_mode = True


class BookResponse(BookBase):
    book_id: int


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
