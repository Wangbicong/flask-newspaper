from flask import render_template, request
from . import main_blueprint
from ..models import Record, User, Newspaper


@main_blueprint.route('/', methods=['get', 'post'])
def index():
    phone_num = request.args.get('phone_num')
    news_name = request.args.get('news_name')
    jou_id = request.args.get('jou_id')

    news_id = request.args.get('news_id')
    user_id = request.args.get('user_id')


    user_data = []
    if phone_num:
        for user in User.query.filter_by(phone_num=phone_num).all():
            user_data.append(user.to_json())
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
    else:
        for news in Newspaper.query.all():
            news_data.append(news.to_json())
    return render_template('index.html', news_data=news_data,
                           user_data=user_data)
