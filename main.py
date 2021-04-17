from flask import Flask
from data.db_session import create_engine, global_init


app = Flask(__name__)


if __name__ == '__main__':
    global_init('store.db')
    app.run()