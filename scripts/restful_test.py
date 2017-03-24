# -*- coding:utf-8 -*-
from requests import get, post, patch

HOST = 'http://localhost:5000/api'


def post_reader():
    print post(HOST+'/reader', json={
        'person_key': 'ewafew13102319',
        'phone_number': '18800463845'
    }).content


def post_news_record():
    print post(HOST+'/news_record', json={
        'person_key': 'ewafew13102319',
        'journal_id': 1,
        'area': u'黑龙江',
        'location': u'黑龙江省哈尔滨市南岗区西大直街92号'
    }).content


def patch_update_packet_status():
    print patch(HOST+'/packet_record', json={
        'person_key': 'ewafew13102319',
        'packet_id': 1
    }).status_code

if __name__ == '__main__':
    # post_reader()
    # post_news_record()
    patch_update_packet_status()