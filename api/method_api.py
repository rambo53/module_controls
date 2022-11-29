from flask import Blueprint, request
from services.method_service import get_methods_service, get_method_service, add_method_service, update_method_service

method_route = Blueprint('method', __name__)

@method_route.route("/methods", methods=['GET'])
def get_methods():
    return get_methods_service()

@method_route.route("/method/<id_public>", methods=['GET'])
def get_method(id_public):
    return get_method_service(id_public)

@method_route.route("/method", methods=['POST'])
def add_method():
    data = request.get_json()
    return add_method_service(data)

@method_route.route("/method/<id_public>", methods=['POST'])
def add_method(id_public):
    data = request.get_json()
    return update_method_service(id_public, data)
