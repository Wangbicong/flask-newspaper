from flask_restful import Api, Resource
from . import main_blueprint

api = Api(main_blueprint)


class HelloWorld(Resource):
    def get(self):
        return 'Hello World'

api.add_resource(HelloWorld, '/')

