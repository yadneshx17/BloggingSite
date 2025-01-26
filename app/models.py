from .database import Base, engine
from sqlalchemy import Column, String, Integer, Text, Boolean, text
from sqlalchemy.sql.sqltypes import TIMESTAMP
# from sqlalchemy import Table, MetaData

# metadata = MetaData()
# my_table = Table('users', metadata, autoload_with=engine)


class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    published = Column(Boolean, server_default=text("true"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    full_name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

# When using alembic no need for manual way.
# This is a manual way to initialize tables in the database by running Base.metadata.create_all(bind=engine) in your code.
# Base.metadata.create_all(bind=engine)
