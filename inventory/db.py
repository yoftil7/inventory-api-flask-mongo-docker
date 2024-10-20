import os,sys
import pymongo
import datetime
import string
import pytz
import sqlite3
import random
import traceback
import json
import csv
from collections import OrderedDict

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_mongodb():


    ret_obj, error_obj = {}, {}
    try:
        conn_str, db_name, ser = "", "", ""
        ser = current_app.config["SERVER"] if "SERVER" in current_app.config else ser
        ser = os.environ["SERVER"] if "SERVER" in os.environ else ser
        if ser == "dev":
            conn_str =  current_app.config["MONGODB_CONNSTRING"]
            db_name = current_app.config["DB_NAME"]
        else:
            conn_str, db_name = os.environ['MONGODB_CONNSTRING'], os.environ['DB_NAME']
        client = pymongo.MongoClient(conn_str)
        client.server_info()
        ret_obj = client[db_name]
    except pymongo.errors.ServerSelectionTimeoutError as err:
        error_obj = {"status":0, "error":"Connection to MongoDB failed", "details":err.details}
    except pymongo.errors.OperationFailure as err:
        error_obj = {"status":0, "error":"Connection to MongoDB failed", "details":err.details}
    return ret_obj, error_obj



