from flask import render_template, request, session, redirect, url_for, jsonify
from flask_restful import Resource, reqparse
from . import main_blueprint, api
from ..models import Record, User, Newspaper
import hashlib

USERNAME = 'root'
PASSWORD = 'root'

m = hashlib.md5()
m.update(USERNAME+PASSWORD)
LOGIN =  m.hexdigest()

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True)
parser.add_argument('password', type=str, required=True)

@main_blueprint.route('/', methods=['get'])
def index():
    if session.get('login', None) == LOGIN:
        phone_num = request.args.get('phone_num')
        news_name = request.args.get('news_name')
        jou_id = request.args.get('jou_id')

        news_id = request.args.get('news_id')
        user_id = request.args.get('user_id')


        user_data = []
        if phone_num:
            for user in User.query.filter_by(phone_num=phone_num).all():
                user_data.append(user.to_json())
        elif news_id:
            for record in Record.query.filter_by(news_id=news_id).all():
                user_data.append(User.query.filter_by(id=record.user_id).first())
        else:
            for user in User.query.all():
                user_data.append(user.to_json())

        news_data = []
        if news_name and jou_id:
            for news in Newspaper.query.filter_by(name=news_name,
                                            jou_id=jou_id).all():
                news_data.append(news.to_json())
        elif news_name:
            for news in Newspaper.query.filter_by(name=news_name).all():
                news_data.append(news.to_json())
        elif jou_id:
            for news in Newspaper.query.filter_by(jou_id=jou_id).all():
                news_data.append(news.to_json())
        elif user_id:
            for record in Record.query.filter_by(user_id=user_id).all():
                news_data.append(Newspaper.query.filter_by(id=record.news_id).first())
        else:
            for news in Newspaper.query.all():
                news_data.append(news.to_json())
        return render_template('index.html', news_data=news_data,
                               user_data=user_data)
    else:
        return redirect('/login/')


@main_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('signin.html')
    else:
        args = parser.parse_args()

        m = hashlib.md5()
        m.update(args['username'] + args['password'])
        LOGIN = m.hexdigest()

        session['login'] = LOGIN
        return redirect('/')
# class LoginAPI(Resource):
#     def get(self):
#         return render_template('index.html', news_data=[],
#                                user_data=[])
#
#     def post(self):
#         args = parser.parse_args()
#         print args
#         return redirect('/')
#
# api.add_resource(LoginAPI, '/login/')




