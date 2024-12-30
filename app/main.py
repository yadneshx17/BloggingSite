from fastapi import Depends, FastAPI
from .database import get_db
from sqlalchemy.orm import Session
import psycopg2
from .routers import blogs, users, auth

app = FastAPI()

app.include_router(blogs.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def root(db: Session = Depends(get_db)):
    return {"message": "Blogging Site"}