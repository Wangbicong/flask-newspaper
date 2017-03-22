from newspaper.models import NewspaperRecord
from flask_restful import Resource, reqparse, fields, marshal_with

news_record_parser = reqparse.RequestParser()
news_record_parser.add_argument('wechat_key', type=str, required=True)
news_record_parser.add_argument('location', type=unicode, required=True)
news_record_parser.add_argument('journal_id', type=int, required=True)
news_record_parser.add_argument('news_name', type=unicode, required=True)

news_record_fields = {
    'wechat_key': fields.String,
    'journal_id': fields.Integer,
    'news_name': fields.String,
    'location': fields.String
}


class NewsRecordApi(Resource):

    @marshal_with(news_record_fields)
    def get(self):
        return NewspaperRecord.get_news_records()

    @marshal_with(news_record_fields)
    def post(self):
        args = news_record_parser.parse_args()
        return NewspaperRecord.add_news_record(**args)
