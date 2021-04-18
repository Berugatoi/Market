from sqlalchemy import Column, Integer, String, Boolean, Date
from .db_session import Base
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date


class UserTable(Base, SerializerMixin):
    __tablename__ = 'user_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    birthday = Column(Date)
    created_date = Column(Date, default=date.today())
    hashed_password = Column(String)
    email = Column(String)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password_hash(self, password):
        return check_password_hash(self.hashed_password, password)
