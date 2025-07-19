from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def listar_libros():
    return {"mensaje": "Aquí irá la lista de libros"}

