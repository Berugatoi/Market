from flask_restful import reqparse


# Для добавления и изменения пользователей
user_parser = reqparse.RequestParser()
user_parser.add_argument("name", required=False)
user_parser.add_argument("surname", required=False)
user_parser.add_argument('email', required=False)
user_parser.add_argument('password', required=False)




