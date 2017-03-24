# -*- coding:utf-8 -*-
from flask import request, jsonify
from newspaper.main import main_bp


@main_bp.route('/wechat', methods=['get'])
def wechat():
    return jsonify(request.args)


@main_bp.route('/wechat/download', methods=['get'])
def download_app():
    pass
