# -*- coding: utf-8 -*-
from flask import redirect
from newspaper.main import main_bp


@main_bp.route('/')
def index():
    return redirect('/admin')


@main_bp.route('/qrcode')
def qrcode():
    return redirect('/admin')