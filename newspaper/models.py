# -*- coding: utf-8 -*-
from datetime import datetime
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
    wallet = db.Column(db.Integer, default=0)
    news_records = db.relationship('NewspaperRecord', backref='reader',
                                   lazy='dynamic')
    red_packet_records = db.relationship('RedPacketRecord', backref='reader',
                                   lazy='dynamic')

    def __init__(self, wechat_key, phone_number=None):
        self.wechat_key = wechat_key
        self.phone_number = phone_number

    def __repr__(self):
        return '%s' % self.wechat_key

    @staticmethod
    def add_reader(**kwargs):
        reader = Reader(**kwargs)
        db.session.add(reader)
        db.session.commit()
        return reader

    @staticmethod
    def get_readers():
        return Reader.query.all()

    @staticmethod
    def update_wallet():
        pass


class Newspaper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    journal_id = db.Column(db.Integer)
    name = db.Column(db.String(20))
    news_records = db.relationship('NewspaperRecord', backref='news',
                                   lazy='dynamic')

    def __init__(self, journal_id, name):
        self.journal_id = journal_id
        self.name = name

    def __repr__(self):
        return '%s——%s' % (self.journal_id, self.name)

    @staticmethod
    def get_newspaper():
        return Newspaper.query.all()

    @staticmethod
    def add_newspaper(**kwargs):
        news = Newspaper(**kwargs)
        db.session.add(news)
        db.session.commit()
        return news


class NewspaperRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reader_id = db.Column(db.Integer, db.ForeignKey('reader.id'))
    news_id = db.Column(db.Integer, db.ForeignKey('newspaper.id'))
    location = db.Column(db.String(50))
    receive_time = db.Column(db.DateTime)

    def __init__(self, location, wechat_key, journal_id, news_name):
        self.location = location
        self.receive_time = datetime.utcnow()

        reader = Reader.query.filter_by(wechat_key=wechat_key).first_or_404()
        self.reader = reader

        news = Newspaper.query.filter_by(journal_id=journal_id, name=news_name).first_or_404()
        self.news = news

    @staticmethod
    def get_news_records():
        return NewspaperRecord.query.all()

    @staticmethod
    def add_news_record(**kwargs):
        news_record = NewspaperRecord(**kwargs)
        db.session.add(news_record)
        db.session.commit()
        return news_record


class RedPacketRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reader_id = db.Column(db.Integer, db.ForeignKey('reader.id'))
    money = db.Column(db.Integer)
    receive_time = db.Column(db.DateTime)