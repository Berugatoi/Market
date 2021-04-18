from flask import Flask
from data.db_session import create_session, global_init
from init_functions import *
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


if __name__ == '__main__':
    global_init('store.db')
    create_base_categories()
    create_base_sex()
    create_base_shoe_size()
    create_base_clothe_size()
    app.run()