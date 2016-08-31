# -*-coding:utf8 -*-
from flask import request, jsonify
from flask_restful import Resource, reqparse
from . import api
from .. import db
from ..parse import date_parse
from ..models import Record, User, Newspaper
import time

parser = reqparse.RequestParser()
parser.add_argument('name', type=unicode, required=True)
parser.add_argument('station', type=unicode, required=True)
parser.add_argument('jou_id', type=int, required=True)


class RecordsAPI(Resource):
    def get(self):
        records = []
        for record in Record.query.all():
            records.append(record.to_json())
        return jsonify(records)


class RecordAPI(Resource):
    '''User的id为user的phone number'''
    def get(self, id):
        user_id = User.query.filter_by(phone_num=id).first().id
        news_id = Newspaper.query.filter_by(name=request.args.get('name'),
                                            jou_id=request.args.get('jou_id')).first().id
        record = Record.query.filter_by(user_id=user_id, news_id=news_id).first()

        if record:
            date = date_parse(record.date)
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
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        record = Record(user_id=user_id, news_id=news_id, station=args['station'], date=date)
        db.session.add(record)


api.add_resource(RecordsAPI, '/record/')
api.add_resource(RecordAPI, '/record/<int:id>/')