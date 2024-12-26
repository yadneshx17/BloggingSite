from fastapi import Depends, FastAPI
from .database import get_db
from sqlalchemy.orm import Session
import psycopg2

app = FastAPI()

cursor = psycopg2.connect('postgresql://postgres:Yadnesh%40017@localhost:5432/blog_site')

@app.get("/")
def root(db: Session = Depends(get_db)):
    return {"message": "Blogging Site"}