from flask import Flask
from flask_restful import Resource, Api, reqparse
from user_model import UsersModel

app = Flask(__name__)
api = Api(app)
users_args = reqparse.RequestParser()
users_args.add_argument('user_name')
users_args.add_argument('user_password')
users = UsersModel()


class Users(Resource):
    def get(self):
        return users.get_users()

    def post(self):
        args = users_args.parse_args()
        print(args)
        user = users.set_users(args.get('user_name'), args.get('user_password'))
        return user


api.add_resource(Users, '/user')

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # flask run --cert=adhoc
