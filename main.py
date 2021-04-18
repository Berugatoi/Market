from flask import Flask, render_template
from data.db_session import create_session, global_init
from init_functions import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/signup')
def singup():
    return render_template('signup.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/viewprofile')
def viewprofile():
    return render_template('view_profile.html')


@app.route('/editprofile')
def editprofile():
    return render_template('login.html')

if __name__ == '__main__':
    global_init('store.db')
    create_base_categories()
    create_base_sex()
    create_base_shoe_size()
    create_base_clothe_size()
    app.run()