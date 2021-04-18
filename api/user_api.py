from flask_restful import reqparse, abort, Api, Resource
from data import db_session as db_sess
from data.user_table import UserTable
from flask import jsonify, make_response
from api.parser import user_parser


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
        sess.query(UserTable).get(user_id).delete()
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
        sess = db_sess.create_session()
        args = user_parser.parse_args()
        user = UserTable(**args)
        return jsonify({'success': "ok"})
