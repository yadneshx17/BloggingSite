from fastapi import Depends, FastAPI, Form
from .database import get_db
from sqlalchemy.orm import Session
import psycopg2
from .routers import blogs, users, auth
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware

    
app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(blogs.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def root(db: Session = Depends(get_db)):
    return {"message": "Blogging Site"}