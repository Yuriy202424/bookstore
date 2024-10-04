from sqlalchemy import select
from main import app
from ..db import Session, Book
from ..schemas import BookData


@app.post('/create')
def create_book(data: BookData):
    with Session.begin() as session:
        book = Book(**data.model_dump())
        session.add(book)
        return book