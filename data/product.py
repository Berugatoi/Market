from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .db_session import Base
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship, backref


class Product(Base, SerializerMixin):
    __tablename__ = 'product_table'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    category = Column(ForeignKey('category_table.id'))
    sex = Column(ForeignKey('sex_table.id'))
    price = Column(Integer)
    size = Column(ForeignKey("shoe_size_table.id"))
    amount = Column(Integer)
    photo = Column(String)
    category_obj = relationship('CategoryTable', backref='products')
    sex_obj = relationship('SexTable')
    size_obj = relationship('ShoeSizeTable')

