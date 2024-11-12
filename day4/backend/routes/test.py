from flask_restful import Resource
from flask import jsonify
# def index():

#     return 'Hello World'

class HelloWorld(Resource):
    def get(self, num):
        return {'hello': 'world', 'number_passed': num}

class Class_Index(Resource):
    def get(self):
        return 'Hello World'
    
    def post(self):
        return 'Hello World, post request received'
    

    def put(self, num):
        print('num:', num)
        return 'Hello World, put request received'
    
    def delete(self):
        return 'Hello World, delete request received'