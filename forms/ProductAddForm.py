from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired
from data import db_session
from data.category import CategoryTable
from data.db_session import global_init
from data.sex_table import SexTable
from data.clothing_size_table import ClothingSizeTable
from flask_wtf.file import FileField, FileRequired


class ProductAddForm(FlaskForm):
    global_init("store.db")
    sess = db_session.create_session()
    choices = [(i.id, i.name) for i in sess.query(CategoryTable).all()]
    name = StringField('name', validators=[DataRequired()])
    category = SelectField('category', validators=[DataRequired()], choices=choices)
    choices = [(i.id, i.name) for i in sess.query(SexTable).all()]
    sex = SelectField('sex', validators=[DataRequired()], choices=choices)
    price = IntegerField('price', validators=[DataRequired()])
    choices = [(i.id, i.size) for i in sess.query(ClothingSizeTable).all()]
    size = SelectField('size', validators=[DataRequired()], choices=choices)
    amount = IntegerField('amount', validators=[DataRequired()])
    photo = FileField('photo', validators=[FileRequired()])
    submit = SubmitField()