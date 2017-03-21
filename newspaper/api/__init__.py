from flask import Blueprint
from flask_restful import Api
from reader import ReaderApi

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')
api = Api(api_bp)

api.add_resource(ReaderApi, '/reader')

import reader