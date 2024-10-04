from sqlalchemy.orm import Mapped
from .. import Base


class Book(Base):
    __tablename__ = "books"

    title: str
    author: str
    content: str