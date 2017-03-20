# -*- coding: utf-8 -*-
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
admin = Admin(name=u'报社管理系统', template_mode='bootstrap3')


def create_app(config_object='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    admin.init_app(app)

    from newspaper.models import User, Reader, Newspaper, \
        NewspaperRecord, RedPacketRecord
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Reader, db.session))
    admin.add_view(ModelView(Newspaper, db.session))
    admin.add_view(ModelView(NewspaperRecord, db.session))
    admin.add_view(ModelView(RedPacketRecord, db.session))

    db.create_all(app=app)

    return app

app = create_app()

import newspaper.views