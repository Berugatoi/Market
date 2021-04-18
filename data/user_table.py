from sqlalchemy import Column, Integer, String, Boolean, Date
from .db_session import Base


class UserTable(Base):
    __tablename__ = 'user_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    birthday = Column(Date)
    created_date = Column(Date)
    hashed_password = Column(String)
    email = Column(String)
