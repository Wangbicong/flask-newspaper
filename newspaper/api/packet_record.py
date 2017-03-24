from newspaper.models import RedPacketRecord
from flask_restful import Resource, reqparse, fields, marshal_with

packet_record_parser = reqparse.RequestParser()
packet_record_parser.add_argument('person_key', type=str, required=True)
packet_record_parser.add_argument('packet_id', type=int, required=True)

packet_record_fields = {
    'reader_id': fields.Integer,
    'money': fields.Integer,
    'receive_time': fields.DateTime,
}


class RedPacketRecordApi(Resource):

    @marshal_with(packet_record_fields)
    def get(self):
        return RedPacketRecord.get_packet_records()

    def patch(self):
        args = packet_record_parser.parse_args()
        return RedPacketRecord.update_status(**args)

