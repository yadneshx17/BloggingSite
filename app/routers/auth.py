from fastapi import APIRouter, Depends, HTTPException, status, Response
from .. import schemas, utils
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User
from ..oauth2 import create_access_token, verify_access_token
from ..schemas import UserCreate, UserOut
from ..utils import get_password_hash


router = APIRouter(tags=['Authentication'])

@router.post("/login", response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_credentials.username).first()

    if not user: 
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials"
        )
    # this is the data we decide to put in the payload: "user_id"
    access_token = create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register/", status_code=status.HTTP_201_CREATED)
def register(user_info: UserCreate, db: Session = Depends(get_db)):

    # Hashing the password
    hashed_password  = get_password_hash(user_info.password)
    user_info.password = hashed_password

    new_user = User(**user_info.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user 