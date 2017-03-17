# -*- coding: utf-8 -*-
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
admin = Admin(name='microblog', template_mode='bootstrap3')


def create_app(config_object='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    admin.init_app(app)

    from newspaper.models import User
    admin.add_view(ModelView(User, db.session))


    return app

app = create_app()

import newspaper.views