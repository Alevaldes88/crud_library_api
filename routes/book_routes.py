from fastapi import APIRouter
from controllers import book_controllers
from models.book_models import Book
router = APIRouter()

@router.get("/", status_code=200)
async def get_books():
    return await book_controllers.get_all_books()

