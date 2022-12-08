from controls.model.method_model import Method
from flask import jsonify, make_response
import uuid
from app import db


def get_methods_service():
    try:
        methods = Method.query.all()
        list_methods = []
        for method in methods:
            dict_method={
                'id':method.id_public,
                'method_name':method.method_name,
                'public_name':method.public_name,
                'need_args':method.need_args,
            }
            list_methods.append(dict_method)
        return jsonify(list_methods)
    except Exception as e:
        return make_response({'message' : str(e)}, 404)


def get_method_service(id_public):
    try:
        method = Method.query.filter(Method.id==id_public).first_or_404()
        model = {
            'name': method.method_name
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
