from flask import Flask, render_template, jsonify, make_response, request, redirect
from data.db_session import create_session, global_init
from init_functions import *
from flask_restful import Api
from api.user_api import UserResource, UserListResource
from requests import get, post


app = Flask(__name__)
api = Api(app)
api.add_resource(UserResource, "/api/user/<user_id>")
api.add_resource(UserListResource, '/api/user')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        print(request.form['password'], request.form['confirm_password'])
        if request.form['password'] != request.form['confirm_password']:
            return render_template('signup.html', password_ok=False, email_ok=True)
        required_data = ['name', 'surname', 'email', 'birthday', 'password']
        data = {k: v for k, v in request.form.items() if k in required_data}
        users = get('http://127.0.0.1:5000/api/user').json()['users']
        if any(i['email'] == data['email'] for i in users):
            return render_template('signup.html', email_ok=False, password_ok=True)
        res = post('http://127.0.0.1:5000/api/user', data=data)
        return redirect('/login')
    return render_template('signup.html', email_ok=True, password_ok=True)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/viewprofile')
def viewprofile():
    return render_template('view_profile.html')


@app.route('/editprofile')
def editprofile():
    return render_template('login.html')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == '__main__':
    global_init('store.db')
    create_base_categories()
    create_base_sex()
    create_base_shoe_size()
    create_base_clothe_size()
    app.run()