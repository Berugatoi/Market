from flask_restful import reqparse, abort, Api, Resource
from data import db_session as db_sess
from data.user_table import UserTable
from flask import jsonify, make_response
from api.parser import user_parser
from datetime import datetime


def abort_if_news_not_found(user_id):
    session = db_sess.create_session()
    news = session.query(UserTable).get(user_id)
    if not news:
        abort(404, message=f"User #{user_id} not found")


class UserResource(Resource):
    def get(self, user_id):
        abort_if_news_not_found(user_id)
        sess = db_sess.create_session()
        user = sess.query(UserTable).get(user_id)
        return jsonify({'user': user.to_dict()})

    def put(self, user_id):
        abort_if_news_not_found(user_id)
        args = user_parser.parse_args()
        sess = db_sess.create_session()
        user = sess.query(UserTable).get(user_id)
        user.name = args.get('name', user.name)
        user.surname = args.get('surname', user.surname)
        user.email = args.get('email', user.email)
        if args.get('password', False):
            user.set_password(args['password'])

    def delete(self, user_id):
        abort_if_news_not_found(user_id)
        sess = db_sess.create_session()
        user = sess.query(UserTable).filter(UserTable.id == user_id).first()
        print(user)
        sess.delete(user)
        sess.commit()
        return jsonify({'success': "ok"})


class UserListResource(Resource):
    def get(self):
        sess = db_sess.create_session()
        users = sess.query(UserTable).all()
        if not users:
            return make_response(jsonify({'error': 'Not found'}), 404)
        return jsonify({'users': [item.to_dict() for item in users]})

    def post(self):
        print('aoskdo[as')
        sess = db_sess.create_session()
        args = user_parser.parse_args()
        required_data = ['name', 'surname', 'password',
                         'birthday', 'email', 'address',
                         'phone_number']
        if not args:
            return make_response(jsonify(error="Empty request"), 400)
        if not all([i in args.keys() for i in required_data]):
            return make_response(jsonify(error="Bad request"), 400)
        user = UserTable(
            name=args['name'],
            surname=args['surname'],
            birthday=datetime.strptime(args['birthday'], "%Y-%m-%d"),
            email=args['email'],
            address=args['address'],
            phone_number=args['phone_number']
        )
        print(args.get('password'))
        user.set_password(args['password'])
        sess.add(user)
        sess.commit()
        return jsonify({'success': "ok"})
