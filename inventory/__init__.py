import os
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from flask_restx import Api, Resource, fields

from .record import api as record_api


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    #CORS(app, supports_credentials=True)
    CORS(app)

    api = Api(app, version='1.0', title='Inventory APIs', description='Documentation for Inventory APIs',)
    api.add_namespace(record_api)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #if app.config["ENV"] == "production":
    #    app.config.from_pyfile('config.prd.py', silent=True)
    #else:
    #    app.config.from_pyfile('config.dev.py', silent=True)
    app.config.from_pyfile('config.dev.py', silent=True)
    jwt = JWTManager(app)



    app.add_url_rule('/', endpoint='index')



    return app
