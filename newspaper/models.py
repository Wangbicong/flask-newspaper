# -*- coding: utf-8 -*-
from newspaper import db, admin


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))

    def __init__(self, username, password):
        self.username = username
        self.password = password


if __name__ == '__main__':
    from newspaper import create_app
    db.create_all(app=create_app())