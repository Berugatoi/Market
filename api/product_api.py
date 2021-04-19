from flask_restful import reqparse, abort, Api, Resource
from data import db_session as db_sess
from data.category import CategoryTable
from flask import jsonify, make_response
from api.parser import user_parser
from datetime import datetime
from api.parser import product_parser
from data.product import Product


class ProductResource(Resource):
    def get(self, product_id):
        sess = db_sess.create_session()
        product = sess.query(CategoryTable).filter(CategoryTable.id == product_id).all()
        if not product:
            return make_response(jsonify(error='Not Found'), 404)
        return jsonify(product=product.to_dict(only=('name', 'category', 'size', 'price', 'sex')))

    def delete(self, product_id):
        sess = db_sess.create_session()
        product = sess.query(CategoryTable).filter(CategoryTable.id == product_id).all()
        if not product:
            return make_response(jsonify(error='Not Found'), 404)
        sess.delete(product)
        sess.commit()
        return jsonify(success='ok')

    def put(self, product_id):
        sess = db_sess.create_session()
        product = sess.query(CategoryTable).filter(CategoryTable.id == product_id).all()
        if not product:
            return make_response(jsonify(error='Not Found'), 404)
        args = product_parser.parse_args()
        product.price = args.get('price', product.price)
        product.category = args.get('category', product.category)
        product.size = args.get('size', product.size)
        product.name = args.get('name', product.name)
        sess.merge(product)
        sess.commit()
        return jsonify(success="ok")


class ProductListResource(Resource):
    def get(self):
        sess = db_sess.create_session()
        products = sess.query(Product).all()
        if not products:
            return make_response(jsonify(error='Not found'), 404)
        return jsonify(products=[item.to_dict() for item in products])

    def post(self):
        sess = db_sess.create_session()
        args = product_parser.parse_args()
        required_data = ['name', 'sex', 'category', 'size', 'price']
        if not args:
            return make_response(jsonify(error='Empty request'), 400)
        if not all([i in args.keys() for i in required_data]):
            return make_response(jsonify(error='Bad request'), 400)
        product = Product()
        product.name = args['name']
        product.size = args['size']
        product.price = args['price']
        product.category = args['cate']
        product.sex = args['sex']
        sess.add(product)
        return jsonify(success='ok')
