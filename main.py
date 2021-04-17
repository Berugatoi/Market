from flask import Flask
from data.db_session import create_session, global_init
from data.category import  CategoryTable
from data.sex_table import SexTable
from data.shoe_size_table import ShoeSizeTable
from data.clothing_size_table import ClothingSizeTable


def create_base_categories():
    sess = create_session()
    categories = ["Брюки", "Худи", "Рубашки", "Куртки", "Брюки спортивные",
                  "Толстовки", "Футболки", "Джинсы", "Джемперы", "Пиджаки",
                  "Костюмы спортивные", "Плащи", "Носки", "Ветровки",
                  "Свитшоты", "Шорты", "Кардиганы", "Пальто",
                  "Ботинки", "Домашняя обувь", "Кроссовки", "Кеды",
                  "Мокасины", "Резиновая обувь", "Сандали", "Сапоги",
                  "Слипоны", "Туфли", "Пуховики"]
    for cat in categories:
        if not sess.query(CategoryTable).filter(CategoryTable.name == cat).first():
            sess.add(CategoryTable(name=cat))
            sess.commit()


def create_base_sex():
    sess = create_session()
    sex = ['Девочка', "Мальчик", "Мужчина", "Женщина"]
    for s in sex:
        if not sess.query(SexTable).filter(SexTable.name == s).first():
            sess.add(SexTable(name=s))
            sess.commit()


def create_base_shoe_size():
    sess = create_session()
    sizes = [str(i) for i in range(20, 48)]
    for size in sizes:
        if not sess.query(ShoeSizeTable).filter(ShoeSizeTable.size == size).first():
            sess.add(ShoeSizeTable(size=size))
            sess.commit()


def create_base_clothe_size():
    sess = create_session()
    sizes = ["XS", "S", "M", "L", "XL", 'XXL', "XXXL"]
    for size in sizes:
        if not sess.query(ClothingSizeTable).filter(ClothingSizeTable.size == size).first():
            sess.add(ClothingSizeTable(size=size))
            sess.commit()


app = Flask(__name__)


if __name__ == '__main__':
    global_init('store.db')
    create_base_categories()
    create_base_sex()
    create_base_shoe_size()
    create_base_clothe_size()
    app.run()