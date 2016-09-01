# -*-coding:utf8 -*-
from flask import jsonify, redirect
from flask_restful import Resource, reqparse
from . import api
from .. import db
from ..models import Newspaper
from requests import get

parser = reqparse.RequestParser()
parser.add_argument('jou_id', type=str, required=True)
parser.add_argument('sub_jou_id', type=str, required=True)
parser.add_argument('name', type=unicode, required=True)
parser.add_argument('pub_date', type=str, required=True)


class NewspapersAPI(Resource):
    def get(self):
        newspapers = []
        for news in Newspaper.query.all():
            newspapers.append(news.to_json())
        return jsonify(newspapers)

    def post(self):
        args = parser.parse_args()
        news = Newspaper(**args)
        db.session.add(news)
        return redirect('/')

    def delete(self):
        return 'delete'


class NewspaperAPI(Resource):
    def get(self, id):
        return 'get'
        # return str(Newspaper.query.filter_by(jou_id=id).first())

    def delete(self, id):
        news = Newspaper.query.filter_by(id=id).first()
        db.session.delete(news)
        return jsonify({'status': 200})

api.add_resource(NewspapersAPI, '/newspaper/')
api.add_resource(NewspaperAPI, '/newspaper/<id>/')
