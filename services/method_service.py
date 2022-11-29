from model.method_model import Method
from flask import jsonify, make_response
import uuid
from app import db

def get_methods_service():
    dict_methods = {}
    try:
        methods = Method.query.all()
        for method in methods:
            dict_methods[method.id]={
                'name':method.name,
                'method_name':method.method_name,
                'details': method.details,
                'number_of_args': method.number_of_args
            }

        return jsonify(dict_methods)
    except Exception as e:
        return make_response({'message' : str(e)}, 404)

def get_method_service(id_public):
    try:
        method = Method.query.filter(Method.id==id_public).first_or_404()
        model = {
            'name': method.name
        }
        return jsonify(model)
    except Exception as e:
        return jsonify({'message' : str(e), 'status': 404}) 

def add_method_service(data):
    try:
        method = Method()
        method.id = str(uuid.uuid4())
        method.name = data['name']
        method.method_name = data['method_name']
        method.details = data['details']
        db.session.add(method)
        db.session.commit()
        
    except Exception as e:
        return jsonify({'message' : str(e), 'status': 404}) 

def update_method_service(id_public, data):
    try:
        method = Method.query.filter(Method.id==id_public).first_or_404()
        method.name = data['name']
        method.method_name = data['method_name']
        method.details = data['details']
        db.session.add(method)
        db.session.commit()
        
    except Exception as e:
        return jsonify({'message' : str(e), 'status': 404}) 
