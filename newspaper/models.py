# -*- coding: utf-8 -*-
import MySQLdb
from flask import abort
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
    person_key = db.Column(db.String(40), unique=True, nullable=False)
    phone_number = db.Column(db.String(11))
    name = db.Column(db.String(20))
    sex = db.Column(db.String(1))
    wallet = db.Column(db.Integer, default=0)
    news_records = db.relationship('NewspaperRecord', backref='reader',
                                   lazy='dynamic')
    red_packet_records = db.relationship('RedPacketRecord', backref='reader',
                                   lazy='dynamic')

    def __init__(self, person_key, phone_number=None):
        self.person_key = person_key
        self.phone_number = phone_number

    def __repr__(self):
        return '%s' % self.person_key

    @staticmethod
    def add_reader(**kwargs):
        reader = Reader(**kwargs)
        db.session.add(reader)
        try:
            db.session.commit()
        except Exception:
            abort(404)
        return reader

    @staticmethod
    def get_readers():
        return Reader.query.all()

    @staticmethod
    def update_wallet():
        pass


class Newspaper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    journal_id = db.Column(db.Integer, nullable=False)
    area = db.Column(db.String(20), nullable=False)
    publish_date = db.Column(db.Date)
    news_records = db.relationship('NewspaperRecord', backref='news',
                                   lazy='dynamic')

    def __init__(self, journal_id, area, publish_time):
        self.journal_id = journal_id
        self.area = area
        self.publish_time = publish_time

    def __repr__(self):
        return '%s——%s' % (self.area, self.journal_id)

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

    def __init__(self, location, person_key, journal_id, area):
        self.location = location
        self.receive_time = datetime.now()

        reader = Reader.query.filter_by(person_key=person_key).first_or_404()
        self.reader = reader

        news = Newspaper.query.filter_by(journal_id=journal_id, area=area).first_or_404()
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
    status = db.Column(db.Boolean, default=False)

    def __init__(self, money, person_key):
        self.money = money

        reader = Reader.query.filter_by(person_key=person_key).first_or_404()
        self.reader = reader

    @staticmethod
    def get_packet_records():
        return RedPacketRecord.query.all()

    @staticmethod
    def add_packet_record(**kwargs):
        packet_record = RedPacketRecord(**kwargs)
        db.session.add(packet_record)
        db.session.commit()
        return packet_record

    @staticmethod
    def update_status(person_key, packet_id):
        packet_record = RedPacketRecord.query.filter_by(id=packet_id).first_or_404()
        if packet_record.reader.person_key == person_key:
            packet_record.status = True
            packet_record.receive_time = datetime.now()
            db.session.add(packet_record)
            db.session.commit()