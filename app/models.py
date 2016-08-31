# -*-coding:utf8 -*-
import json
from app import db
from parse import date_parse, sex_parse


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
        return json.dumps(self.to_json())

    def to_json(self):
        return {
            'id': self.__dict__['id'],
            'jou_id': self.__dict__['jou_id'],
            'sub_jou_id': self.__dict__['sub_jou_id'],
            'name': self.__dict__['name'],
            'pub_date': str(self.__dict__['pub_date'])
        }


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
        return json.dumps(self.to_json())

    def to_json(self):
        return{
            'id': self.__dict__['id'],
            'phone_num': self.__dict__['phone_num'],
            'name': self.__dict__['name'],
            'sex': sex_parse(self.__dict__['sex'], True),
            'age': self.__dict__['age'],
            'address': self.__dict__['address']
        }


class Record(db.Model):
    __tablename__ = 'records'
    id = db.Column(db.Integer, primary_key=True)
    news_id = db.Column(db.Integer,
                        db.ForeignKey('newspapers.id'))
    user_id = db.Column(db.Integer,
                          db.ForeignKey('users.id'))
    station = db.Column(db.String(100), nullable=True)
    date = db.Column(db.DateTime, nullable=True)

    def __init__(self, news_id, user_id, station=None, date=None):
        self.news_id = news_id
        self.user_id = user_id
        self.station = station
        self.date = date

    def __repr__(self):
        return json.dumps(self.to_json())

    def to_json(self):
        return {
            'news_id': self.__dict__['news_id'],
            'user_id': self.__dict__['user_id'],
            'station': self.__dict__['station'],
            'date': date_parse(self.__dict__['date'])
        }


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
