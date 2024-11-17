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
    
class testCelery(Resource):
    def get(self):
        from celery_tasks import celeryIndex, plus, dbUpdate, dbQuery, reminder, html
        # task1 = dbUpdate.delay()
        task1 = reminder.delay()
        task2 = html.delay()
        task2.wait()
        # task2 = plus.delay(1, 2)
        # while not task2.ready():
        #     pass
        # task2.wait()
        from flask import jsonify
        # return jsonify({"task1_id": task1.id, "task2_id": task2.id, "task1_result": task1.get(), "task2_result": task2.get(), "message": "success", "status": task1.status, "status2": task2.status})
        return jsonify({"task1_id": task1.id, "task1_result": task1.get(), "message": "success", "status": task1.status})