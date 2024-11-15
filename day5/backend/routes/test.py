from flask_restful import Resource
from flask import jsonify
from flask_security import auth_token_required, roles_accepted
# def index():

#     return 'Hello World'

class HelloWorld(Resource):
    @auth_token_required
    def get(self, num):
        return {'hello': 'world', 'number_passed': num}

class Class_Index(Resource):
    @auth_token_required
    def get(self):
        return 'Hello World'
    
    @auth_token_required
    @roles_accepted('admin')
    def post(self):
        return 'Hello World, post request received'

    @auth_token_required
    @roles_accepted('admin', 'manager')    
    def put(self, num):
        print('num:', num)
        return 'Hello World, put request received'
    
    @auth_token_required
    @roles_accepted('admin')
    def delete(self):
        return 'Hello World, delete request received'