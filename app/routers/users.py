from fastapi import Depends, APIRouter, HTTPException, Response, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User
from ..schemas import UserCreate, UserOut
from ..utils import get_password_hash

# router = APIRouter()

router = APIRouter(
    tags=['Users']
)

# get user
@router.get("/users/{id}", response_model=UserOut)
def get_user(id: int, db : Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} does not exit")
    return user 

# # create users - replaced to register user in auth file. 
# @router.post("/users/", status_code=status.HTTP_201_CREATED)
# def create_user(user_info: UserCreate, db: Session = Depends(get_db)):

#     # Hashing the password
#     hashed_password  = get_password_hash(user_info.password)
#     user_info.password = hashed_password

#     new_user = User(**user_info.model_dump())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# Deleting User
@router.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)):    
    user = db.query(User).filter(User.id==id)
    deleted_user = user.first()

    if not deleted_user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    user.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Update USer
@router.put("/users/{id}")
def update_user(id: int, updated_user: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id==id)
    new_user = user.first()

    if not new_user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    user.update(updated_user.model_dump(), synchronize_session=False)
    db.commit()
    return user.first()