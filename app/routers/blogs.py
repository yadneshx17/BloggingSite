from ..models import Blog
from sqlalchemy.orm import Session
from app.database import get_db
from fastapi import Depends, HTTPException, Response, status
from fastapi import APIRouter

from ..schemas import BLogcreate, BlogOut

"""
204 status code should be when the item is not found which means your request processed successfully and the content not found.
404 status code automatically appears when the requested API is unavailable. Links that lead to a 404 page are often called broken or dead links and can be subject to link rot.

"""

router = APIRouter(tags=['Blogs'])

#get blog
@router.get("/blogs/", response_model=list[BlogOut])
def get_blogs(db: Session = Depends(get_db)):
    blog = db.query(Blog).all()
    if not blog:
        return {"message": "blog does not exist"}
    return blog

#get blog by id
@router.get("/blogs/{id}", response_model=list[BlogOut])
def get_blog_by_id(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id==id).all()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="blog does not exist")
    return blog

# create blog
@router.post("/blogs/")
def create_blogs(data: BLogcreate, db: Session = Depends(get_db)):
    new_blog = Blog(**data.model_dump())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# Delete Blogs
@router.delete("/blogs/{id}")
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id==id)
    deleted_blog = blog.first()

    if not deleted_blog:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog does not exist")
    
    blog.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Update Blog
@router.put("/blogs/{id}")
def update_blog(id: int, updated_blog: BLogcreate, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id)
    new_blog = blog.first()

    if not new_blog: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog does not exist")
    
    blog.update(updated_blog.model_dump(), synchronize_session=False)
    db.commit()
    return blog.first()