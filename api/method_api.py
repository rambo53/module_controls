from flask import Blueprint, request
from services.method_service import get_methods_service

method_route = Blueprint('method', __name__)

@method_route.route("/methods", methods=['GET'])
def get_methods():
    return get_methods_service()