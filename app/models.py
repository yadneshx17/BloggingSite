from .database import Base, engine
from sqlalchemy import Column, String, Integer, Text

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

# class User(Base):
#     __tablename__ = "votes"


# This is a manual way to initialize tables in the database by running Base.metadata.create_all(bind=engine) in your code.
Base.metadata.create_all(bind=engine)