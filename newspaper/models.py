# -*- coding: utf-8 -*-
from newspaper import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Reader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wechat_key = db.Column(db.String(40), unique=True, nullable=False)
    phone_number = db.Column(db.String(11))
    name = db.Column(db.String(20))
    sex = db.Column(db.String(1))
    wallet = db.Column(db.Integer, default=0, nullable=False)

    def __init__(self, wechat_key):
        self.wechat_key = wechat_key


class Newspaper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    journal_id = db.Column(db.Integer)
    name = db.Column(db.String(20))

    def __init__(self, journal_id, name):
        self.journal_id = journal_id
        self.name = name


class NewspaperRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(50))
    receive_time = db.Column(db.DateTime)


class RedPacketRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    money = db.Column(db.Integer)
    receive_time = db.Column(db.DateTime)


if __name__ == '__main__':
    from newspaper import create_app
    db.create_all(app=create_app())