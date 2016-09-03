# -*- coding:utf-8 -*-
import codecs
import xlrd
from . import db
from models import User, Record, Newspaper


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
        args = {
            'phone_num': int(rows[4]),
            'name': rows[0],
            'sex': rows[1],
            'age': int(rows[2]),
            'address': rows[3],
            'status': rows[5]
        }
        user = User(**args)
        db.session.add(user)

if __name__ == '__main__':
    import_user()

