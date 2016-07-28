from os.path import sep
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config.from_object('config')
    app.config.from_pyfile('../instance/config.py'.replace('/', sep))

    Bootstrap(app)
    db.init_app(app)

    from models import Newspaper, User, Record
    db.create_all(app=app)

    from .main import main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app

