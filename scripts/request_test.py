# -*- coding:utf8 -*-
from requests import get, post, put, delete

host = 'localhost:5000'
# host = '123.56.41.206'
#
# data = {
#     'jou_id': 154,
#     'sub_jou_id': 124,
#     'name': '人民日报',
#     'pub_date': '2014-01-01'
# }
# print put('http://localhost:5000/api/newspaper/', data=data)
#


def user_test():
    print get('http://%s/api/user/13782472197/' % host).content

    data = {
        'phone_num': '13782472197'
    }
    print put('http://%s/api/user/' % host, data=data)

    date = {
        'phone_num': '1234545454',
        'sex': None,
        'age': None,
        'name': None,
        'address': None
    }
    print post('http://%s/user/' % host, data=data)

    print delete('http://127.0.0.1:5000/newspaper/1/').content

def record_test():
    print get('http://%s/api/record/13782472197/?name=人民日报&jou_id=1' % host).content

    data = {
        'name': '人民日报',
        'jou_id': '1',
        'station': '如家快捷酒店'
    }
    print put('http://%s/api/record/13782472197/' % host, data=data)

if __name__ == '__main__':
    user_test()
    record_test()