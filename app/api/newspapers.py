# -*-coding:utf8 -*-
from flask_restful import Resource
from . import api
from app.models import Newspaper


class NewspapersAPI(Resource):
    def get(self):
        return str(Newspaper.query.all())

    def post(self):
        return 'post'

    def put(self):
        return 'put'

    def delete(self):
        return 'delete'


class NewspaperAPI(Resource):
    def get(self, id):
        return str(Newspaper.query.filter_by(jou_id=id).first())

    def post(self):
        return 'post'

    def put(self):
        return 'put'

    def delete(self):
        return 'delete'

api.add_resource(NewspapersAPI, '/newspaper/')
api.add_resource(NewspaperAPI, '/newspaper/<int:id>')
