from pydantic import BaseModel, EmailStr
from typing import Optional


class BLogcreate(BaseModel):
    title: str
    content: str
    published: bool = True

    class Config:
        extra = "forbid"

    # # by default
    # class Config:
    #     extra = "ignore"

class UserCreate(BaseModel):
    email: EmailStr # EmailStr - validates that its a email and not just normal text
    username: str
    password: str
    
# ------------------------------------------------------

# RESPONSE MODELS

class BlogOut(BaseModel):
    # other fileds are inherited from postbase
    id: int
    title: str
    content: str

    class Config:
        from_attributes  = True

class UserOut(BaseModel):
    id: int 
    email: EmailStr
    username: str
    class Config:
        from_attributes  = True

class UserLogin(BaseModel):
    email: EmailStr
    token_type: str

# Validating the Token
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None