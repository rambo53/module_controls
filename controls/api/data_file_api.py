from flask import Blueprint, request
from controls.services.data_file_service import get_data_files_service

data_file_route = Blueprint('data_file', __name__)

@data_file_route.route("/data_files", methods=['GET'])
def get_data_files():
    return get_data_files_service()