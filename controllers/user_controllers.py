from db.config import get_conexion
from models.user_models import User, UserCreate
from fastapi import HTTPException
import aiomysql


async def get_all_users():
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute('SELECT * FROM library.users')
            usersList = await cursor.fetchall()
            return usersList
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    finally:
        conn.close()

async def get_user_by_id(user_id: int):
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute("SELECT * FROM library.users WHERE id=%s", (user_id,))
            user = await cursor.fetchone()
            if not user:
                raise HTTPException(
                    status_code=404, detail='Usuario no encontrado')
            else:
                return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    finally:
        conn.close()


async def update_user(user_id: int, user: User):
    if user_id != user.id:
        raise HTTPException(status_code=400, detail='El ID no coincide')
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute("UPDATE library.users SET name=%s, age=%s, surname=%s, mail=%s, status=%s, password=%s, rol=%s WHERE id=%s", (
                user.name,
                user.age,
                user.surname,
                user.mail,
                user.status,
                user.password,
                user.rol,
                user_id
            ))
            await conn.commit()
            user = await get_user_by_id(user_id)
            return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    finally:
        conn.close()


async def delete_by_id(user_id: int):
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            # verificar el usuario existe.
            user = await get_user_by_id(user_id)
            if not user:
                raise HTTPException(
                    status_code=404, detail='Usuario no existe')
            # Eliminar el usuario
            await cursor.execute('DELETE FROM library.users WHERE id=%s', (user_id,))
            await conn.commit()
            return {"msg": f"Usuario con id {user_id} eliminado correctamente", "status": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
    finally:
        conn.close()


