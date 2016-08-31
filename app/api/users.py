# -*- coding:utf8 -*-
from flask import jsonify
from flask_restful import Resource, reqparse
from ..models import User
from ..qr_code import create_qrcode
from .. import db
from . import api

parser = reqparse.RequestParser()
parser.add_argument('phone_num', type=int, required=True)
# parser.add_argument('name', type=unicode, required=True)
# parser.add_argument('sex', type=int, required=True)
# parser.add_argument('age', type=int, required=True)
# parser.add_argument('address', type=unicode, required=True)


class UsersAPI(Resource):
    def get(self):
        users = []
        for user in User.query.all():
            users.append(user.to_json())
        return jsonify(users)

    def put(self):
        args = parser.parse_args()
        user = User(**args)
        db.session.add(user)
        # db.session.commit()


class UserAPI(Resource):
    '''id为user的phone number'''
    def get(self, id):
        create_qrcode(User.query.filter_by(phone_num=id).first())
        return jsonify(login_state=bool(User.query.filter_by(phone_num=id).first()))


api.add_resource(UsersAPI, '/user/')
api.add_resource(UserAPI, '/user/<int:id>/')