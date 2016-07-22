from flask import Blueprint
from flask_restful import Api

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

from .views import *
from .newspapers import *
from .users import *
from .records import *