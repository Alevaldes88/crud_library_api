from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
    isbn: str
    year: int
    publisher: str
    genre: str
    language: str
    status: bool
    pages: int

class BookCreate(BaseModel):
    title: str
    author: str
    isbn: str
    year: int
    publisher: str
    genre: str
    language: str
    status: bool
    pages: int