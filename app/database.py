from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

# print(SQLALCHEMY_DATABASE_URL)

# makes database connection 
engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()

# facilitate interaction with database
SessionLocal = sessionmaker(autocommit=False, 
autoflush=False, bind=engine)

# provides session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  