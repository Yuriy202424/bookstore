from pydantic import BaseModel


class BookData(BaseModel):
    id: int
    author: str
    content: str