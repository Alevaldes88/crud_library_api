from fastapi import APIRouter
from controllers import user_controllers
from models.user_models import User


router = APIRouter()


@router.get('/', status_code=200)
async def get_all():
    return await user_controllers.get_all_users()

# Obtener usuarios por id http://localhost:8000/users/{user_id}
@router.get('/{user_id}', status_code=200)
async def get_user_by_id(user_id: int):
    return await user_controllers.get_user_by_id(user_id)


# Borrar un usuario por id http://localhost:800/books/{user_id}
@router.delete('/{user_id}', status_code=200)
async def delete_by_id(user_id: int):
    return await user_controllers.delete_by_id(user_id)

# Actualizar un usuario http://localhost:800/users/{user_id}
@router.put('/{user_id}', status_code=200)
async def update_user(user_id: int, user: User):
    return await user_controllers.update_user(user_id, user)