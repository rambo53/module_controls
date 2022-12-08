from flask import Blueprint, request
from controls.services.data_file_service import get_data_files_service, add_data_files_service, get_data_file_service

data_file_route = Blueprint('data_file', __name__)

@data_file_route.route("/data_files", methods=['GET'])
def get_data_files():
    return get_data_files_service()

@data_file_route.route("/data_file/<id_public>", methods=['GET'])
def get_data_file(id_public):
    return get_data_file_service(id_public)

@data_file_route.route("/data_file", methods=['POST'])
def add_data_files():
    new_file = request.files['newFile']
    return add_data_files_service(new_file)
