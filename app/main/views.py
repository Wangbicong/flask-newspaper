from flask import render_template
from flask_restful import Api, Resource
from . import main_blueprint

api = Api(main_blueprint)


class HelloWorld(Resource):
    def get(self):
        return render_template('main.html')

api.add_resource(HelloWorld, '/')

