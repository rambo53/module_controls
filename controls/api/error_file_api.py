from flask import Blueprint, request
from controls.services.error_file_service import add_error_file_service, get_error_file_service

error_file_route = Blueprint('error_file', __name__)

@error_file_route.route("/<name>", methods=['GET'])
def get_error_file(name):
    return get_error_file_service(name)

@error_file_route.route("/launch_controls", methods=['POST'])
def add_error_file():
    data = request.get_json()
    return add_error_file_service(data)

