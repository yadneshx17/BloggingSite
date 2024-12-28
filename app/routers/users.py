from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User

router = APIRouter()

@router.get("/users")
def get_user(db : Session = Depends(get_db)):
    user = db.query(User).all()
    if not user: 
        return {"message": "user not found"}
    return {"data": user} 