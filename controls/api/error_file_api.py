from flask import Blueprint, request
from controls.services.error_file_service import get_error_files_service

error_file_route = Blueprint('error_file', __name__)

@error_file_route.route("/error_files", methods=['GET'])
def get_error_files():
    return get_error_files_service()