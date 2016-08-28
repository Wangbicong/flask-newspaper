# -*-coding:utf8 -*-
import json
from app import db


class Newspaper(db.Model):
    __tablename__ = 'newspapers'
    id = db.Column(db.Integer, primary_key=True)
    jou_id = db.Column(db.Integer, nullable=False)
    sub_jou_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    pub_date = db.Column(db.Date, nullable=False)

    def __init__(self, jou_id, sub_jou_id, name, pub_date):
        self.jou_id = jou_id
        self.sub_jou_id = sub_jou_id
        self.name = name
        self.pub_date = pub_date

    def __repr__(self):
        # datetime需要格式化为字符串形式
        dict = {}
        dict['jou_id'] = int(self.__dict__['jou_id'])
        dict['sub_jou_id'] = int(self.__dict__['sub_jou_id'])
        dict['name'] = (self.__dict__['name'])
        dict['pub_date'] = str(self.__dict__['pub_date'].year) + '-' + \
                           str(self.__dict__['pub_date'].month) + '-' + str(self.__dict__['pub_date'].day)
        return json.dumps(dict)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    phone_num = db.Column(db.String(11), nullable=False)
    name = db.Column(db.String(4), nullable=True)
    sex = db.Column(db.Boolean, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    address = db.Column(db.String(40), nullable=True)

    def __init__(self, phone_num, name=None, sex=None, age=None, address=None):
        self.phone_num = phone_num
        self.name = name
        self.sex = sex
        self.age = age
        self.address = address

    def __repr__(self):
        dict = {}
        dict['phone_num'] = str(self.__dict__['phone_num'])
        dict['name'] = (self.__dict__['name'])
        dict['sex'] = int(self.__dict__['sex'])
        dict['age'] = int(self.__dict__['age'])
        dict['address'] = (self.__dict__['address'])
        return json.dumps(dict)


class Record(db.Model):
    __tablename__ = 'records'
    id = db.Column(db.Integer, primary_key=True)
    news_id = db.Column(db.Integer,
                        db.ForeignKey('newspapers.id'))
    user_id = db.Column(db.Integer,
                          db.ForeignKey('users.id'))
    station = db.Column(db.String(40), nullable=True)
    date = db.Column(db.Date, nullable=True)

    def __init__(self, news_id, user_id, station, date):
        self.news_id = news_id
        self.user_id = user_id
        self.station = station
        self.date = date

    def __repr__(self):
        # datetime需要格式化为字符串形式
        dict = {}
        dict['news_id'] = int(self.__dict__['news_id'])
        dict['user_id'] = int(self.__dict__['user_id'])
        dict['station'] = (self.__dict__['station'])
        dict['date'] = str(self.__dict__['date'].year) + '-' + \
                           str(self.__dict__['date'].month) + '-' + str(self.__dict__['date'].day)
        return json.dumps(dict)


class Subscription(db.Model):
    __tablename__ = 'subscriptions'
    id = db.Column(db.Integer, primary_key=True)
    news_id = db.Column(db.Integer,
                        db.ForeignKey('newspapers.id'))
    user_id = db.Column(db.Integer,
                          db.ForeignKey('users.id'))

    def __init__(self, news_id, user_id, station):
        self.news_id = news_id
        self.user_id = user_id

    def __repr__(self):
        dict = {}
        dict.update(self.__dict__)
        for key in dict.keys():
            if key[0] == '_':
                del dict[key]
        return str(dict)
