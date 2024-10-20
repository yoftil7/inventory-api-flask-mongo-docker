import os,sys
from flask_restx import Namespace, Resource, fields
from flask import (request, current_app)
from werkzeug.utils import secure_filename
import datetime
import time
import subprocess
import json
from inventory.db import get_mongodb
from pymongo import DESCENDING

api = Namespace("record", description="Record APIs")

search_model = api.model(
    'Record Search', {
        'field': fields.String(required=True, default="", description='search field'),
        'query': fields.String(required=True, default="", description='Search value'),
    }
)

insert_model = api.model(
    'Record Insert', {
        'name': fields.String(required=True, default="James", description='First name'),
        'age': fields.Integer(required=True, description='Age')
    }
)

delete_model = api.model('Record Delete',{
    'row': fields.Integer(required=True, description="Row of item to delete")
    }
)

update_model = api.model('Record Update', {
    'row': fields.Integer(required=True, description='Row of record to update'),
    'key': fields.String(required=True, description='Field to update'),
    'new_value': fields.String(required=True, description='New value')
    }
)


@api.route('/insert')
class RecordList(Resource):
    @api.doc('insert_records')
    @api.expect(insert_model)
    def post(self):
        req_obj = request.json
        mongo_dbh, error_obj = get_mongodb()
        if error_obj != {}:
            return error_obj
        last_doc = mongo_dbh['c_inventory'].find_one(sort=[('_id', DESCENDING)])
        if last_doc:
            current_row = last_doc['row'] + 1
        else:
            current_row = 1
        req_obj['row'] = current_row    
        res = mongo_dbh["c_inventory"].insert_one(req_obj)
        res_obj = {"status":1}
        return res_obj

    @api.doc(False)
    def get(self):
        return self.post()


@api.route('/search')
class RecordList(Resource):
    @api.doc('search_records')
    @api.expect(search_model)
    def post(self):
        req_obj = request.json
        search_field = req_obj.get('field')
        search_query = req_obj.get('query')
        mongo_dbh, error_obj = get_mongodb()
        if error_obj != {}:
            return error_obj
        res_obj = {"records":[]}
        if search_field == 'row' or search_field == 'age':
            search_query = int(search_query)
        if search_field and search_query is not None:
            for doc in mongo_dbh["c_inventory"].find({search_field: search_query}):
                if "_id" in doc:
                    doc["_id"] = str(doc["_id"])
                res_obj["records"].append(doc)
        else: 
            for doc in mongo_dbh["c_inventory"].find():
                if "_id" in doc:
                    doc["_id"] = str(doc["_id"])
                res_obj["records"].append(doc)
           # res_obj["records"] = list(mongo_dbh["c_inventory"].find())
        
        res_obj["status"] = 1
        return res_obj

    @api.doc(False) 
    def get(self):
        return self.post()


@api.route('/delete')
class RecordList(Resource):
    @api.doc('delete_records')
    @api.expect(delete_model)
    def delete(self):
        req_obj = request.json
        if 'row' not in req_obj:
            return {'status': 0, 'message': 'Missing row in request'}, 400
        mongo_dbh, error_obj = get_mongodb()
        if error_obj != {}:
            return error_obj
        delete_obj = {'row': req_obj.get('row')}
        res = mongo_dbh['c_inventory'].delete_one(delete_obj)
        if res.deleted_count == 1:
            return {'status': 1, 'message': 'Record successfully deleted'}
        else: 
            return {'status': 0, 'message': 'Record not found!'}

    @api.doc(False)
    def get(self):
        return self.delete()


@api.route('/update')
class RecordList(Resource):
    @api.doc('update_records')
    @api.expect(update_model)
    def put(self):
        req_obj = request.json
        mongo_dbh, error_obj = get_mongodb()
        if error_obj:
            return error_obj
        update_row = req_obj.get('row')
        update_key = req_obj.get('key')
        new_value = req_obj.get('new_value')
        if update_key == 'age' or update_key == 'row':
            new_value = int(new_value)
        update_res = mongo_dbh['c_inventory'].update_one({"row": update_row}, {"$set": {update_key: new_value}})
        if update_res.modified_count == 1:
            return {'status': 1, 'message': 'Update successful'}
        else:
            return {'status': 0, 'message': 'Record not updated'}
        
    @api.doc(False)
    def get(self):
        return self.put()









