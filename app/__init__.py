import os
from flask import Flask
from flask_restx import Api
from werkzeug.middleware.proxy_fix import ProxyFix
from .extensions import db, api
from .resources import ns

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    api.init_app(app)
    db.init_app(app)
    with app.app_context():
        # db.drop_all()
        db.create_all()
    api.add_namespace(ns)

    return app
