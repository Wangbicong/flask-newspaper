# -*- coding:utf-8 -*-
import codecs
import xlrd
from datetime import date
from . import db
from models import User, Newspaper, Record


def output_news():
    with codecs.open('app/temp/result.csv', 'w',encoding='gbk') as f:
        f.write(u'报纸名称,总期数,期数,发行日期\n')

        for news in Newspaper.query.all():
            data = news.to_json()
            f.write(unicode(data['name'])+','+unicode(data['jou_id'])+','
                    +unicode(data['sub_jou_id'])+','+unicode(data['pub_date'])+'\n')


def output_user():
    with codecs.open('app/temp/result.csv', 'w', encoding='gbk') as f:
        f.write(u'姓名,手机号,年龄,性别,住址,核实结果\n')

        for user in User.query.all():
            data = user.to_json()
            f.write(unicode(data['name']) + ',' + unicode(data['phone_num']) + ','
                    + unicode(data['age']) + ',' + unicode(data['sex']) + ',' + unicode(data['address'])
                    + ',' + unicode(data['status']) + '\n')


def import_user():
    workbook = xlrd.open_workbook('app/temp/readers.xlsx')

    sheet = workbook.sheet_by_index(0)
    for i in xrange(1, sheet.nrows):
        rows = sheet.row_values(i)
        phone_num = int(rows[4])
        args = {
            'phone_num': int(phone_num),
            'name': rows[0],
            'sex': rows[1],
            'age': int(rows[2]),
            'address': rows[3],
            'status': rows[5]
        }
        user = User.query.filter_by(phone_num=phone_num).first()
        if not user:
            user = User(**args)
        else:
            user.address = args['address']
            user.name = args['name']
            user.age = args['age']
            user.status = args['status']
            user.sex = args['sex']
        db.session.add(user)


def import_newspaper():
    workbook = xlrd.open_workbook('app/temp/newspapers.xlsx')

    sheet = workbook.sheet_by_index(0)
    for i in xrange(1, sheet.nrows):
        rows = sheet.row_values(i)
        jou_id = rows[1]
        name = rows[0]
        pub_date = date(*xlrd.xldate_as_tuple(rows[3], workbook.datemode)[:3]).strftime('%Y-%m-%d')
        args = {
            'jou_id': jou_id,
            'sub_jou_id': rows[2],
            'name': name,
            'pub_date': pub_date
        }
        if not Newspaper.query.filter_by(name=name, jou_id=jou_id).first():
            news = Newspaper(**args)
            db.session.add(news)


def output_news_2(id):
    with codecs.open('app/temp/result.csv', 'w',encoding='gbk') as f:
        f.write(u'报纸名称,总期数,期数,发行日期\n')

        for record in Record.query.filter_by(user_id=id).all():
            data = Newspaper.query.filter_by(id=record.news_id).first()
            data = data.to_json()
            f.write(unicode(data['name']) + ',' + unicode(data['jou_id']) + ','
                    + unicode(data['sub_jou_id']) + ',' + unicode(data['pub_date']) + '\n')


def output_record(id):
    with codecs.open('app/temp/result.csv', 'w',encoding='gbk') as f:
        f.write(u'领取人姓名,领取号码,领取地点,领取时间\n')

        for record in Record.query.filter_by(news_id=id).all():
            user = User.query.filter_by(id=record.user_id).first()
            daya = {
                'id': record.id,
                'name': user.name,
                'phone_num': user.phone_num,
                'station': record.station,
                'date': record.date
            }
            f.write(unicode(user.name) + ',' + unicode(user.phone_num) + ','
                    + unicode(record.station) + ',' + unicode(record.date) + '\n')

if __name__ == '__main__':
    import_user()

