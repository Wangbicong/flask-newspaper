# -*-coding:utf8 -*-
from flask import jsonify
from flask_restful import Resource, reqparse
from . import api
from .. import db
from ..models import Newspaper

parser = reqparse.RequestParser()
parser.add_argument('jou_id', type=int, required=True)
parser.add_argument('sub_jou_id', type=int, required=True)
parser.add_argument('name', type=unicode, required=True)
parser.add_argument('pub_date', type=str, required=True)


class NewspapersAPI(Resource):
    def get(self):
        newspapers = []
        for news in Newspaper.query.all():
            newspapers.append(news.to_json())
        return jsonify(newspapers)

    def put(self):
        args = parser.parse_args()
        news = Newspaper(**args)
        db.session.add(news)
        return 200

    def delete(self):
        return 'delete'


class NewspaperAPI(Resource):
    def get(self, id):
        return 'get'
        # return str(Newspaper.query.filter_by(jou_id=id).first())

    def post(self):
        return 'post'

    def put(self):
        return 'put'

    def delete(self):
        return 'delete'

api.add_resource(NewspapersAPI, '/newspaper/')
api.add_resource(NewspaperAPI, '/newspaper/<int:id>/')
