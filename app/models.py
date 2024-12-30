from .database import Base, engine
from sqlalchemy import Column, String, Integer, Text, Boolean

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    published = Column(Boolean, nullable=False, default=True)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)


# This is a manual way to initialize tables in the database by running Base.metadata.create_all(bind=engine) in your code.
Base.metadata.create_all(bind=engine)