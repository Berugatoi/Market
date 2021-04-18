from sqlalchemy import Column, Integer, String, Boolean
from .db_session import Base
from sqlalchemy_serializer import SerializerMixin


class SexTable(Base, SerializerMixin):
    __tablename__ = 'sex_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)