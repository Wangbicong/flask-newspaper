# -*-coding:utf8 -*-
from flask import redirect, url_for, send_from_directory, abort
from flask_restful import Resource
from . import api
from ..qr_code import create_qrcode
from ..models import Newspaper
from ..m_csv import create_news, create_user


class QrCodesAPI(Resource):
    def get(self, id):
        create_qrcode(Newspaper.query.filter_by(id=id).first().to_json())
        return send_from_directory('temp/', 'qr_code.png')


class CsvAPI(Resource):
    def get(self, tag):
        if tag == 'newspaper.csv':
            create_news()
        elif tag == 'user.csv':
            create_user()
        else:
            abort(404)
        return send_from_directory('temp/', 'result.csv')

api.add_resource(QrCodesAPI, '/qrcode/<int:id>/')
api.add_resource(CsvAPI, '/csv/<tag>')
