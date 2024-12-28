from ..models import Blog
from sqlalchemy.orm import Session
from app.database import get_db
from fastapi import Depends
from fastapi import APIRouter

router = APIRouter()

#get post
@router.get("/blogs")
def get_blogs(db: Session = Depends(get_db)):
    blog = db.query(Blog).all()
    if not blog:
        return {"message": "blog does not exist"}
    return {"message": blog}

#get post by id
@router.get("/blogs/{id}")
def get_blogs(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id==id).all()
    if not blog:
        return {"message": "Blog does not exist"}
    return {"message": blog}