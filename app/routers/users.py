from fastapi import Depends, APIRouter, HTTPException, Response, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User

router = APIRouter()

# get users
@router.get("/users")
def get_user(db : Session = Depends(get_db)):
    user = db.query(User).all()
    if not user: 
        return {"message": "user not found"}
    return {"data": user} 

# create users
@router.post("/users")
def create_user(user_info: dict, db: Session = Depends(get_db)):
    new_user = User(**user_info)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Deleting User
@router.post("/users/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id==id)
    deleted_user = user.first()

    if not deleted_user: 
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    user.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Update USer
@router.put("/users/{id}")
def update_user(id: int, updated_user: dict, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id==id)
    new_user = user.first()

    if not new_user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    user.update(updated_user, synchronize_session=False)
    db.commit()
    return user.first()