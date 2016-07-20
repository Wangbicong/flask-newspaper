from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config.from_object('config')
    app.config.from_pyfile('..\\instance\\config.py')

    db.init_app(app)

    return app

