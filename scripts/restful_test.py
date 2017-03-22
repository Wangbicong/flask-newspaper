# -*- coding:utf-8 -*-
from requests import get, post, patch

HOST = 'http://localhost:5000/api'


def post_reader():
    print post(HOST+'/reader', json={
        'wechat_key': 'ewafew13103',
        'phone_number': '18800463845'
    }).content


def post_news_record():
    print post(HOST+'/news_record', json={
        'wechat_key': 'ewafew13103',
        'journal_id': 1,
        'news_name': u'人民日报',
        'location': u'黑龙江省哈尔滨市南岗区西大直街92号'
    }).content

if __name__ == '__main__':
    post_reader()
    post_news_record()