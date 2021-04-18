from flask import Flask
from data.db_session import create_session, global_init
from init_functions import *

app = Flask(__name__)


if __name__ == '__main__':
    global_init('store.db')
    create_base_categories()
    create_base_sex()
    create_base_shoe_size()
    create_base_clothe_size()
    app.run()