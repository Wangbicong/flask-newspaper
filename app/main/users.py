# -*- coding:utf8 -*-
from flask import jsonify, redirect, request
from flask_restful import Resource, reqparse
from ..models import User, Record
from .. import db
from . import api

parser = reqparse.RequestParser()
parser.add_argument('phone_num', type=str, required=True)
parser.add_argument('name', type=unicode, required=False)
parser.add_argument('sex', type=unicode, required=False)
parser.add_argument('age', type=str, required=False)
parser.add_argument('address', type=unicode, required=False)
parser.add_argument('status', type=unicode, required=False)


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
        return redirect('/?tab=user')


class UserAPI(Resource):
    '''id为user的phone number'''
    def get(self, id):
        return jsonify(login_state=bool(User.query.filter_by(phone_num=id).first()))

    def post(self, id):
        user = User.query.filter_by(id=id).first()

        args = parser.parse_args()
        for key in args:
            if len(args[key]) == 0:
                args[key] = None

        user.address = args['address']
        user.name = args['name']
        user.age = args['age']
        user.status = args['status']
        user.sex = args['sex']
        user.phone_num = args['phone_num']

        db.session.add(user)

        return redirect('/?tab=user')



    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        for record in Record.query.filter_by(user_id=id).all():
            db.session.delete(record)
        return jsonify({'status':200})


api.add_resource(UsersAPI, '/user/')
api.add_resource(UserAPI, '/user/<int:id>/')
