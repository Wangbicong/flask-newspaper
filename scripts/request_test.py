# -*- coding:utf8 -*-
from requests import get, post, put, delete

# data = {
#     'jou_id': 154,
#     'sub_jou_id': 124,
#     'name': '人民日报',
#     'pub_date': '2014-01-01'
# }
# print put('http://localhost:5000/api/newspaper/', data=data)
#


def user_test():
    print get('http://localhost:5000/api/user/13782472197/').content

    data = {
        'phone_num': '13782472197'
    }
    print put('http://localhost:5000/api/user/', data=data)


def record_test():
    print get('http://localhost:5000/api/record/13782472197/?name=人民日报&jou_id=1').content

    data = {
        'name': '人民日报',
        'jou_id': '1',
        'station': '如家快捷酒店'
    }
    print put('http://localhost:5000/api/record/13782472197/', data=data)

if __name__ == '__main__':
    user_test()
    record_test()