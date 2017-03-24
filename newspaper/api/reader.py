from newspaper.models import Reader
from flask_restful import Resource, reqparse, fields, marshal_with

reader_parser = reqparse.RequestParser()
reader_parser.add_argument('person_key', type=str, required=True)
reader_parser.add_argument('phone_number', type=str)

reader_fields = {
    'person_key': fields.String,
    'phone_number': fields.String
}


class ReaderApi(Resource):

    @marshal_with(reader_fields)
    def get(self):
        return Reader.get_readers()

    @marshal_with(reader_fields)
    def post(self):
        args = reader_parser.parse_args()
        return Reader.add_reader(**args)

    def patch(self):
        pass
