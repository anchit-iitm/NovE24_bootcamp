from flask import jsonify, make_response, request
from models import db, user_datastore
from flask_restful import Resource

class register_api(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return make_response(jsonify({'message': 'data not found, supply json'}), 400)
        present_user = user_datastore.find_user(email=data['emailFromJson'])

        if present_user is None: #if not present_user:

            new_user = user_datastore.create_user(email=data['emailFromJson'], password=data['passwordFromJson'])
            
            if data['roleFromJson'] == 'admin':
                return make_response(jsonify({'message': 'admin role cant be granted'}), 406)
            if data['roleFromJson'] == 'manager':
                user_datastore.add_role_to_user(new_user, 'manager')
                
                user_datastore.deactivate_user(new_user)
                db.session.commit()
                return make_response(jsonify({'message': 'success', "email": data['emailFromJson']}), 201)
            if data['roleFromJson'] == 'customer':
                user_datastore.add_role_to_user(new_user, 'customer')
                db.session.commit()
                return make_response(jsonify({'message': 'success', "email": data['emailFromJson']}), 201)
        
        return make_response(jsonify({'message': 'email id is already registered with us', "email": data['emailFromJson']}), 406)


class login_api(Resource):
    def post(self):
        data = request.get_json()
        if not data:
            return make_response(jsonify({'message': 'data not found, supply json'}), 400)
        present_user = user_datastore.find_user(email=data['emailFromJson'])
        if present_user is None:
            return make_response(jsonify({'message': 'email id is not registered with us', "email": data['emailFromJson']}), 406)
        if present_user.active == True:
            if present_user.password == data['passwordFromJson']:
                auth_token = present_user.get_auth_token()
                from flask_security import login_user
                login_user(present_user)
                db.session.commit()
                return make_response(jsonify({'message': 'login success', "email": data['emailFromJson'], 'authToken': auth_token}), 200)
            return make_response(jsonify({'message': 'login failed, password mismatch', "email": data['emailFromJson']}), 406)
        return make_response(jsonify({'message': 'login failed, user is not active contact admin', "email": data['emailFromJson']}), 406)