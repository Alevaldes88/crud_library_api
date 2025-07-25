from fastapi import FastAPI
from routes import book_routes
from routes import user_routes

app = FastAPI()
app.include_router(book_routes.router,
                   prefix="/books",
                   tags=["Books"])


app.include_router(user_routes.router,
                   prefix="/users",
                   tags=["Users"])