from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .db_session import Base


class ShoeSizeTable(Base):
    __tablename__ = "shoe_size_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    size = Column(String)