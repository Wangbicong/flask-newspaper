# -*-coding:utf8 -*-
from flask import redirect, request, send_from_directory, abort
from flask_restful import Resource
from . import api
from ..qr_code import create_qrcode
from ..models import Newspaper
from ..op_excel import output_news, output_user, import_user, import_newspaper


class QrCodesAPI(Resource):
    def get(self, id):
        create_qrcode(Newspaper.query.filter_by(id=id).first().to_json())
        return send_from_directory('temp/', 'qr_code.png')


class CsvsAPI(Resource):
    def get(self, tag):
        if tag == 'newspaper.csv':
            output_news()
        elif tag == 'user.csv':
            output_user()
        else:
            abort(404)
        return send_from_directory('temp/', 'result.csv')

    def post(self, tag):
        if tag == 'readers.xlsx':
            f = request.files['file']
            f.save('app/temp/readers.xlsx')
            import_user()
            return redirect('/?tab=user')
        else:
            f = request.files['file']
            f.save('app/temp/newspapers.xlsx')
            import_newspaper()
            return redirect('/')

class Csvs2API(Resource):
    def get(self, id, tag):
        # elif tag == 'record.csv':
        #     pass
        # elif tag == 'news.csv':
        #     pass
        pass

api.add_resource(QrCodesAPI, '/qrcode/<int:id>/')
api.add_resource(CsvsAPI, '/csv/<tag>')
api.add_resource(Csvs2API, '/csv/<int:id>/<tag>')
