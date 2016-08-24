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
# data = {
#     'phone_num': '13782472197',
#     'name': '焦冠凯',
#     'sex': 1,
#     'age': 20,
#     'address': '人寿公司家属院'
#
# }
# print put('http://localhost:5000/api/user/', data=data)

data = {
    'name': '人民日报',
    'jou_id': 1

}
print get('http://localhost:5000/api/record/13782472197/?name=人民日报&jou_id=1').content

print get('http://localhost:5000/api/user/13782472197/').content