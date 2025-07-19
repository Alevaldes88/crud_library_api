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


async def get_a_book_by_id(id: int):
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute("SELECT * FROM library.books WHERE id = %s", (id,))
            data = await cursor.fetchone()

        if data:
            return data
        else:
            raise HTTPException(
                status_code=404, detail="Libro no encontrado"
            )

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error: {str(e)}"
        )

    finally:
        conn.close()


    