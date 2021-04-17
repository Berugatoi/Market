from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relation
from data.db_session import Base


class CategoryTable(Base):
    __tablename__ = "category_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
