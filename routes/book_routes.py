from fastapi import APIRouter
from controllers import book_controllers
from models.book_models import Book, BookCreate
router = APIRouter()


# Obtener todos los libros http://localhost:8000/books
@router.get("/", status_code=200)
async def get_books():
    return await book_controllers.get_all_books()

# Obtener libro por id http://localhost:8000/books/{id}
@router.get("/{id}", status_code=200)
async def get_book_by_id(id: int):
    return await book_controllers.get_a_book_by_id(id)

# Borrar un libro por id http://localhost:800/books/{id}
@router.delete("/{id}", status_code=200)
async def delete_book(id: int):
    return await book_controllers.delete_a_book(id)

# Crear un libro http://localhost:800/books
@router.post('/', status_code=201)
async def create_book(book: BookCreate):
    return await book_controllers.create_a_book(book)

# Actualizar un libro http://localhost:800/books/{id}
@router.put('/{id}', status_code=200)
async def update_book(id: int, book: Book):
    return await book_controllers.update_a_book(id, book)



