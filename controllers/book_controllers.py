from db.config import get_conexion
from fastapi import HTTPException
import aiomysql

async def get_all_books():
    try:
        # obtener acceso a la bbdd de forma asincrona
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            # Consultamos los datos
            await cursor.execute('SELECT * FROM library.books')
            # obtener los resultados
            data = await cursor.fetchall()
        return data
    except Exception as e:
        raise HTTPException(
            status_code= 500, detail= f"Error: {str(e)}")
    finally:
        conn.close()