from fastapi import APIRouter
from controllers import book_controllers
from models.book_models import Book
router = APIRouter()


# Obtener todos los libros http://localhost:8000/books
@router.get("/", status_code=200)
async def get_books():
    return await book_controllers.get_all_books()

# Obtener libror por id http://localhost:8000/books/{id}
@router.get("/{id}", status_code=200)
async def get_book_by_id(id: int):
    return await book_controllers.get_a_book_by_id(id)

# Borrar un libro por id http://localhost:800/books/{id}
@router.delete("/{id}", status_code=200)
async def delete_book(id: int):
    return await book_controllers.delete_a_book(id)





