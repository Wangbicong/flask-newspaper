from flask_restful import Resource
from . import api


class HelloWorld(Resource):
    def get(self):
        return 'Welcome to user our api! -- by wbc'

api.add_resource(HelloWorld, '/')
