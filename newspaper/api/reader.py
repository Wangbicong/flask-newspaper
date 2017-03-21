from newspaper.models import Reader
from flask_restful import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('wechat_key', type=str, required=True)
parser.add_argument('phone_number', type=str)


class ReaderApi(Resource):

    def get(self):
        pass

    def post(self):
        args = parser.parse_args()
        Reader.add_reader(**args)
