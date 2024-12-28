from ..models import Blog
from sqlalchemy.orm import Session
from app.database import get_db
from fastapi import Depends, HTTPException, Response, status
from fastapi import APIRouter

router = APIRouter()

#get blog
@router.get("/blogs")
def get_blogs(db: Session = Depends(get_db)):
    blog = db.query(Blog).all()
    if not blog:
        return {"message": "blog does not exist"}
    return {"message": blog}

#get blog by id
@router.get("/blogs/{id}")
def get_blogs(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id==id).all()
    if not blog:
        return {"message": "Blog does not exist"}
    return {"message": blog}

# create blog
@router.post("/blogs")
def create_blogs(data: dict, db: Session = Depends(get_db)):
    new_blog = Blog(**data)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# Delete Blogs
@router.post("/blogs/{id}")
def delete_blogs(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id==id)
    deleted_blog = blog.first()

    if not deleted_blog:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    blog.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Update Blog
@router.put("/blogs/{id}")
def update_blog(id: int, updated_blog: dict, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id)
    new_blog = blog.first()

    if not new_blog: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    blog.update(updated_blog, synchronize_session=False)
    db.commit()
    return blog.first()