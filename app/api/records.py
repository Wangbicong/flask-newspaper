# -*-coding:utf8 -*-
from flask import request, jsonify
from flask_restful import Resource, reqparse
from ..models import Record, User, Newspaper
from . import api


class RecordsAPI(Resource):
    def get(self):
        return str(Record.query.all())


class RecordAPI(Resource):
    '''User的id为user的phone number'''
    def get(self, id):
        user_id = User.query.filter_by(phone_num=id).first_or_404().id
        news_id = Newspaper.query.filter_by(name=request.args.get('name'),
                                            jou_id=request.args.get('jou_id')).first_or_404().id
        if Record.query.filter_by(user_id=user_id, news_id=news_id).first_or_404():
            return jsonify(eval(str(Record.query.filter_by(user_id=user_id).first())))


api.add_resource(RecordsAPI, '/record/')
api.add_resource(RecordAPI, '/record/<int:id>/')