from flask import Flask, render_template, jsonify, make_response, request, redirect, url_for, session
from data import db_session as db_sess
from init_functions import *
from flask_restful import Api
from api.user_api import UserResource, UserListResource
from requests import get, post
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from data.user_table import UserTable
from api.product_api import ProductResource, ProductListResource
from uuid import uuid5, NAMESPACE_OID
from forms.ProductAddForm import ProductAddForm
from werkzeug.utils import secure_filename
from data.product import Product
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from functions import format_image
import os


class UserView(ModelView):
    can_create = False
    column_exclude_list = ["hashed_password", 'birthday', 'created_date']
    column_searchable_list = ['name']


    def is_accessible(self):
        return current_user.is_authenticated

    def unaccessible_callback(self, name, **kwargs):
        return redirect('/login')


class ProductView(UserView):
    column_exclude_list = ['photo']
    column_sortable_list = ['price']


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
admin = Admin(app, name="market", template_mode='bootstrap3')
admin.add_view(UserView(UserTable, db_sess.create_session()))
admin.add_view(ProductView(Product, db_sess.create_session()))

api = Api(app)
api.add_resource(UserResource, "/api/user/<user_id>")
api.add_resource(UserListResource, '/api/user')
api.add_resource(ProductResource, '/api/product/<int:product_id>')
api.add_resource(ProductListResource, '/api/product')
app.secret_key = 'Market_site'
login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/addPhoto", methods=['POST', 'GET'])
def addPhoto():
    form = ProductAddForm()
    if form.validate_on_submit():
        f = form.photo.data
        image = f.read()
        filename = secure_filename(f.filename)
        dst_name = str(uuid5(NAMESPACE_OID, str(image)))
        ext = filename.split('.')[-1].lower()
        name = dst_name + "." + ext
        with open(f'static/img/{name}', "wb") as m:
            m.write(image)
        format_image.resize_image(f'static/img/{name}')
        prod = Product(
            name=form.name.data,
            category=form.category.data,
            sex=form.sex.data,
            price=form.price.data,
            size=form.size.data,
            amount=form.amount.data,
            photo=name
        )
        sess = db_sess.create_session()
        sess.add(prod)
        sess.commit()
    return render_template("addProduct.html", form=form)


@app.route('/prod/<prod_id>')
def get_product(prod_id):
    sess = db_sess.create_session()
    prod = sess.query(Product).filter(Product.id == prod_id).first()
    if not prod:
        return redirect('/')
    return render_template('product.html', product=prod)


@app.route('/changepassword', methods=['POST', 'GET'])
def change_password():
    sess = db_sess.create_session()
    if request.method == 'POST':
        password = request.form['password']
        password_again = request.form['password_again']
        if password_again != password:
            return render_template('change_password.html', error="Пароли не совпадают")
        current_user.set_password(password)
        sess.merge(current_user)
        sess.commit()
        return redirect('/')
    return render_template('change_password.html')


@app.route('/')
def home():
    sess = db_sess.create_session()
    filter = request.cookies.get('filter')
    cat = sess.query(CategoryTable).all()
    if not filter:
        products = sess.query(Product).all()
    else:
        products = sess.query(CategoryTable).filter(CategoryTable.name == filter).first()
        products = products.products
    fav = request.cookies.get('UserCookie', False)
    if fav:
        try:
            fav = list(map(int, request.cookies['UserCookie'].split(':')))
        except TypeError as e:
            pass
    res = make_response(render_template('home.html', products=products, categories=cat, favs=fav))
    res.set_cookie('filter', '', max_age=0)
    return res


@app.route('/favorite')
def favorite_prod():
    cookies = request.cookies.get('UserCookie', False)
    products = []
    if cookies:
        cookies = cookies.split(':')
        sess = db_sess.create_session()
        products = sess.query(Product).filter(Product.id.in_(cookies)).all()
    return render_template('favorites.html', products=products)


@app.route('/cart', methods=['POST', 'GET'])
def card():
    if request.method == 'POST':
        # Форма появляется только если корзина не пустая
        cookies = request.cookies.get("Cart")
        sess = db_sess.create_session()
        for i in cookies.split(':'):
            prod = sess.query(Product).filter(Product.id == i).first()
            if prod.amount > 0:
                prod.amount -= int(request.form[f'quantity_{i}'])
                sess.merge(prod)
                sess.commit()
            prod.amount = max(prod.amount, 0)
        res = make_response(redirect('/'))
        res.set_cookie('Cart', '', max_age=0)
        return res
    cookies = request.cookies.get('Cart', False)
    products = []
    if cookies:
        cookies = [i.split('-')[0] for i in cookies.split(':')]
        sess = db_sess.create_session()
        products = sess.query(Product).filter(Product.id.in_(cookies)).all()
    return render_template('cart.html', products=products)


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        if request.form['password'] != request.form['confirm_password']:
            return render_template('signup.html', password_ok=False, email_ok=True)
        required_data = ['name', 'surname', 'email', 'birthday', 'password', 'address', 'phone_number']
        data = {k: v for k, v in request.form.items() if k in required_data}
        users = get('http://127.0.0.1:5000/api/user').json()
        if users.get('users', False):
            if any(i['email'] == data['email'] for i in users['users']):
                return render_template('signup.html', email_ok=False, password_ok=True)
        res = post('http://127.0.0.1:5000/api/user', data=data)
        return redirect('/login')
    return render_template('signup.html', email_ok=True, password_ok=True)


@login_manager.user_loader
def load_user(user):
    sess = db_sess.create_session()
    user = sess.query(UserTable).filter(UserTable.id == user).first()
    return user


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        sess = db_sess.create_session()
        user = sess.query(UserTable).filter(UserTable.email == email).first()
        if not user:
            return render_template('login.html', error=1)
        if not user.check_password(password):
            return render_template('login.html', error=2)
        login_user(user, remember=True)
        return redirect('/')
    return render_template('login.html')


@app.route('/viewprofile')
@login_required
def viewprofile():
    if not current_user.is_authenticated:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return render_template('view_profile.html', user=current_user)


@app.route('/editprofile', methods=['POST', 'GET'])
@login_required
def editprofile():
    if request.method == 'POST':
        sess = db_sess.create_session()
        new_data = request.form
        current_user.name = new_data['name']
        current_user.surname = new_data['surname']
        current_user.address = new_data['address']
        current_user.email = new_data['email']
        current_user.phone_number = new_data['phone']
        sess.merge(current_user)
        sess.commit()
        return redirect('/viewprofile')
    return render_template('edit_profile.html')


@app.route('/filter/<string:filter>')
def filter_prods(filter):
    sess = db_sess.create_session()
    res = make_response(redirect('/'))
    res.set_cookie('filter', filter)
    return res


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == '__main__':
    db_sess.global_init('store.db')
    create_base_categories()
    create_base_sex()
    create_base_shoe_size()
    create_base_clothe_size()
    app.run()