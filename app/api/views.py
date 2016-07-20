from flask_restful import Api, Resource
from . import api_blueprint

api = Api(api_blueprint)


class Newspaper(Resource):
    def get(self):
        return 'get'

    def post(self):
        return 'post'

    def put(self):
        return 'put'

    def delete(self):
        return 'delete'

api.add_resource(Newspaper, '/')

