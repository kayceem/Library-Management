from database import engine
from sqlalchemy.schema import CreateTable
from sqlalchemy.orm import Session
from database import engine
from models import Base, User, Book, BookDetail, BorrowedBook, Admin
from faker import Faker
import random
import utils

Base.metadata.create_all(bind=engine)
for table in Base.metadata.sorted_tables:
    print(CreateTable(table).compile(engine))


fake = Faker()

session = Session(engine)

for _ in range(10):
    user = User(
        name=fake.name(),
        email=fake.email(),
        membership_date=fake.date_between(start_date="-1y", end_date="today"),
    )
    session.add(user)

for _ in range(10):
    book = Book(
        title=fake.sentence(nb_words=5),
        isbn=fake.unique.random_int(min=10**12, max=10**13 - 1),
        published_date=fake.date_between(start_date="-5y", end_date="today"),
        genre=fake.word(),
    )
    session.add(book)
    session.flush()

    book_detail = BookDetail(
        book_id=book.book_id,
        publisher=fake.company(),
        language=fake.language_name(),
        number_of_pages=fake.random_int(min=50, max=500),
    )
    session.add(book_detail)

users = session.query(User).all()
books = session.query(Book).all()
for _ in range(10):
    book = random.choice(books)
    books.remove(book)
    borrowed_book = BorrowedBook(
        user_id=random.choice(users).user_id,
        book_id=book.book_id,
        borrow_date=fake.date_between(start_date="-1y", end_date="today"),
        return_date=fake.date_between(start_date="today", end_date="+1y"),
    )
    session.add(borrowed_book)

admin = Admin(usernmame="admin", password=utils.hash_password("Password1@"))
session.add(admin)
session.commit()
