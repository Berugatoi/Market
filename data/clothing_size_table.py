from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .db_session import Base


class ClothingSizeTable(Base):
    __tablename__ = "clothe_size_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    size = Column(String)