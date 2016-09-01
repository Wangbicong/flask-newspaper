# -*- coding:utf8 -*-
from flask import jsonify, redirect, request
from flask_restful import Resource, reqparse
from ..models import User
from .. import db
from . import api

parser = reqparse.RequestParser()
parser.add_argument('phone_num', type=str, required=True)
parser.add_argument('name', type=unicode, required=False)
parser.add_argument('sex', type=str, required=False)
parser.add_argument('age', type=str, required=False)
parser.add_argument('address', type=unicode, required=False)


class UsersAPI(Resource):
    def get(self):
        users = []
        for user in User.query.all():
            users.append(user.to_json())
        return jsonify(users)

    def post(self):

        args = parser.parse_args()
        for key in args:
            if len(args[key]) == 0:
                args[key] = None

        user = User(**args)
        db.session.add(user)
        return redirect('/')


class UserAPI(Resource):
    '''id为user的phone number'''
    def get(self, id):
        return jsonify(login_state=bool(User.query.filter_by(phone_num=id).first()))

    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        return redirect('/', code=200)


api.add_resource(UsersAPI, '/user/')
api.add_resource(UserAPI, '/user/<int:id>/')