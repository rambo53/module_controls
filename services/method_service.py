from model.method_model import Method
from flask import jsonify

def get_methods_service():
    methods = Method.query.all()
    dict_methods = {}
    for method in methods:
        dict_methods[method.id]={
            'name':method.name,
            'method_name':method.method_name,
            'details': method.details,
            'number_of_args': method.number_of_args
        }

    return jsonify(dict_methods)