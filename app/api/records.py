# -*-coding:utf8 -*-
from flask_restful import Resource
from app.models import Record
from . import api

class RecordsAPI(Resource):
    def get(self):
        return str(Record.query.all())


class RecordAPI(Resource):
    '''User的id为user的phone number'''
    def get(self, id):
        return str(Record.query.filter_by(phone_num=id).first())


api.add_resource(RecordsAPI, '/record/')
api.add_resource(RecordAPI, '/record/<int:id>')