from db.config import get_conexion
from fastapi import HTTPException
import aiomysql
from models.book_models import Book, BookCreate

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

async def delete_a_book(id: int):
    book = await get_a_book_by_id(id)
    if book:
        # puedo borrar
        try:
            conn = await get_conexion()
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                await cursor.execute("DELETE FROM library.books WHERE id=%s", (id,))
                # tenemos que confirmar la consulta de la linea anterior
                await conn.commit()
                return {'msg': f'El libro con id {id} ha sido eliminado existosamente', 'status': True}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
        finally:
            conn.close()
    else:
        raise HTTPException(
            status_code=404, detail=f'El libro con id {id} no  se ha encontrado')

from fastapi import HTTPException
import aiomysql
from db.config import get_conexion
from models.book_models import BookCreate
from controllers.book_controllers import get_a_book_by_id

async def create_a_book(book: BookCreate):
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            # Validar duplicado por ISBN
            await cursor.execute("SELECT * FROM library.books WHERE isbn = %s", (book.isbn,))
            existe = await cursor.fetchone()
            if existe:
                raise HTTPException(status_code=400, detail="Ya existe un libro con ese ISBN.")

            # Insertar el libro
            await cursor.execute("""
                INSERT INTO library.books 
                (title, author, isbn, year, publisher, genre, language, status, pages)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                book.title,
                book.author,
                book.isbn,
                book.year,
                book.publisher,
                book.genre,
                book.language,
                book.status,
                book.pages
            ))

            await conn.commit()
            nuevo_id = cursor.lastrowid

        # Obtener y retornar el nuevo libro
        libro = await get_a_book_by_id(nuevo_id)
        return {"msg": "Libro insertado correctamente", "item": libro}

    except HTTPException:
        raise  # Re-lanzamos si ya fue lanzado antes
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
    finally:
        conn.close()


async def update_a_book(id: int, book: Book):
    if id != book.id:
        raise HTTPException(status_code=400, detail="Los ID no coinciden")
    try:
        conn = await get_conexion()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute("""
                                UPDATE library.books
                                SET title = %s,
                                    author = %s,
                                    isbn = %s,
                                    year = %s,
                                    publisher = %s,
                                    genre = %s,
                                    language = %s,
                                    status = %s,
                                    pages = %s
                                WHERE id = %s
                            """, (
                                book.title,
                                book.author,
                                book.isbn,
                                book.year,
                                book.publisher,
                                book.genre,
                                book.language,
                                book.status,
                                book.pages,
                                id
                                ))
            await conn.commit()
            # ya tenemos el id de producto lo que tenemos que hacer o responder con el producto actualizado.
            book = await get_a_book_by_id(id)
            return {"msg": 'Libro actualizado correctamente', "item": book}
    except Exception as e:
        raise HTTPException(status_code=500, detail= f"Error: {str(e)}")
    finally:
        conn.close()


