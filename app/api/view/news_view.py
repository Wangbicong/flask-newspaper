from flask_restful import Resource
from app.api import api
from app.api.action.news_manage import *


class Newspapers(Resource):
    def get(self):
        return get_newspapers()

    def post(self):
        return 'post'

    def put(self):
        return 'put'

    def delete(self):
        return 'delete'


class Newspaper(Resource):
    def get(self, id):
        return 'get %r' % id

    def post(self):
        return 'post'

    def put(self):
        return 'put'

    def delete(self):
        return 'delete'

api.add_resource(Newspapers, '/newspaper/')
api.add_resource(Newspaper, '/newspaper/<int:id>')
