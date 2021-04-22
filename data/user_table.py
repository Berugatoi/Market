from sqlalchemy import Column, Integer, String, Boolean, Date, Text
from .db_session import Base
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date
from flask_login import UserMixin


class UserTable(Base, SerializerMixin, UserMixin):
    __tablename__ = 'user_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    birthday = Column(Date)
    created_date = Column(Date, default=date.today())
    hashed_password = Column(String)
    phone_number = Column(String)
    address = Column(Text)
    email = Column(String)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
