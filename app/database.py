from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = f'postgresql://postgres:Yadnesh%40017@localhost:5432/blog_site'

# makes database connection 
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# facilitate interaction with database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# provides session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()