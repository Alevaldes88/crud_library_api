from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    id: Optional[int]
    title: str
    author: str
    isbn: str
    year: int
    publisher: str
    genre: str
    language: str
    status: bool
    pages: int

    class Config:
        orm_mode = True
