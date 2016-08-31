# -*- coding:utf-8 -*-
import codecs
from models import User, Record, Newspaper


def create_news():
    with codecs.open('app/temp/result.csv', 'w',encoding='gbk') as f:
        f.write(u'报纸名称,总期数,期数,发行日期\n')

        for news in Newspaper.query.all():
            data = news.to_json()
            f.write(unicode(data['name'])+','+unicode(data['jou_id'])+','
                    +unicode(data['sub_jou_id'])+','+unicode(data['pub_date'])+'\n')


def create_user():
    with codecs.open('app/temp/result.csv', 'w', encoding='gbk') as f:
        f.write(u'姓名,手机号,年龄,性别,住址\n')

        for user in User.query.all():
            data = user.to_json()
            f.write(unicode(data['name']) + ',' + unicode(data['phone_num']) + ','
                    + unicode(data['age']) + ',' + unicode(data['sex']) + ',' + unicode(data['address'])+'\n')