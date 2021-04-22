from flask_restful import reqparse


# Для добавления и изменения пользователей
user_parser = reqparse.RequestParser()
user_parser.add_argument("name", required=False)
user_parser.add_argument("surname", required=False)
user_parser.add_argument('email', required=False)
user_parser.add_argument('password', required=False)
user_parser.add_argument('birthday', required=False)
user_parser.add_argument('address', required=False)
user_parser.add_argument('phone_number', required=False)


product_parser = reqparse.RequestParser()
product_parser.add_argument('name', required=False)
product_parser.add_argument('sex', required=False)
product_parser.add_argument('category', required=False)
product_parser.add_argument('price', required=False)
