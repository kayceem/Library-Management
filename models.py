from database import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy import Column, Integer, BigInteger, String, ForeignKey, Date


class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    membership_date = Column(
        TIMESTAMP(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False,
    )


class Book(Base):
    __tablename__ = "book"
    book_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    isbn = Column(BigInteger, unique=True, nullable=False)
    published_date = Column(
        Date,
        nullable=False,
    )
    genre = Column(String(255), unique=False, nullable=False)


class BookDetail(Base):
    __tablename__ = "book_detail"
    details_id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(
        Integer,
        ForeignKey("book.book_id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    )
    publisher = Column(String(255), nullable=False)
    language = Column(String(255), nullable=False)
    number_of_pages = Column(Integer, nullable=False)

    book = relationship(
        "Book", foreign_keys=[book_id], backref=backref("book_detail"), uselist=False
    )


class BorrowedBook(Base):
    __tablename__ = "borrowed_book"
    user_id = Column(
        Integer,
        ForeignKey("user.user_id", ondelete="CASCADE"),
        nullable=False,
        primary_key=True,
    )
    book_id = Column(
        Integer,
        ForeignKey("book.book_id", ondelete="CASCADE"),
        nullable=False,
        primary_key=True,
        unique=True,
    )
    borrow_date = Column(
        Date,
        nullable=False,
    )
    return_date = Column(
        Date,
    )
    user = relationship(
        "User",
        foreign_keys=[user_id],
        backref=backref("borrowed_books", cascade="all, delete-orphan"),
    )
    book = relationship(
        "Book",
        foreign_keys=[book_id],
        backref=backref("borrow_detail", cascade="all, delete-orphan"),
        uselist=False,
    )
