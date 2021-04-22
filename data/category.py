from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relation
from .db_session import Base
from sqlalchemy_serializer import SerializerMixin


class CategoryTable(Base, SerializerMixin):
    __tablename__ = "category_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
