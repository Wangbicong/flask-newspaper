# -*-coding:utf8 -*-
from flask import request, jsonify
from flask_restful import Resource, reqparse
from . import api
from .. import db
from ..models import Record, User, Newspaper
import datetime

parser = reqparse.RequestParser()
parser.add_argument('name', type=unicode, required=True)
parser.add_argument('station', type=unicode, required=True)
parser.add_argument('jou_id', type=int, required=True)


class RecordsAPI(Resource):
    def get(self):
        return str(Record.query.all())


class RecordAPI(Resource):
    '''User的id为user的phone number'''
    def get(self, id):
        user_id = User.query.filter_by(phone_num=id).first().id
        news_id = Newspaper.query.filter_by(name=request.args.get('name'),
                                            jou_id=request.args.get('jou_id')).first().id
        record = Record.query.filter_by(user_id=user_id, news_id=news_id).first()
        if bool(record):
            date = str(record.date.year) + '-' + \
                           str(record.date.month) + '-' + str(record.date.day)
            return jsonify(receive_state=bool(record), news_num=len(Record.query.filter_by(user_id=user_id).all()),
                       date=date, station=record.station)
        else:
            return jsonify(receive_state=bool(record), news_num=len(Record.query.filter_by(user_id=user_id).all()),
                   date=None, station=None)

    def put(self, id):
        args = parser.parse_args()
        user_id = User.query.filter_by(phone_num=id).first().id
        news_id = Newspaper.query.filter_by(name=args['name'],
                                            jou_id=args['jou_id']).first().id
        date = str(datetime.date.today())
        record = Record(user_id=user_id, news_id=news_id, station=args['station'], date=date)
        db.session.add(record)


api.add_resource(RecordsAPI, '/record/')
api.add_resource(RecordAPI, '/record/<int:id>/')