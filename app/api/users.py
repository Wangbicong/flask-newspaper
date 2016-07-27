# -*- coding:utf8 -*-
from flask import jsonify
from flask_restful import Resource, reqparse
from app.models import User
from app import db
from . import api

parser = reqparse.RequestParser()
parser.add_argument('phone_num', type=int, required=True)
parser.add_argument('name', type=unicode, required=True)
parser.add_argument('sex', type=int, required=True)
parser.add_argument('age', type=int, required=True)
parser.add_argument('address', type=unicode, required=True)


class UsersAPI(Resource):
    def get(self):
        return jsonify(eval(str(User.query.all())))

    def put(self):
        args = parser.parse_args()
        news = User(**args)
        db.session.add(news)
        db.session.commit()


class UserAPI(Resource):
    '''id为user的phone number'''
    def get(self, id):
        return str(User.query.filter_by(phone_num=id).first())


api.add_resource(UsersAPI, '/user/')
api.add_resource(UserAPI, '/user/<int:id>')