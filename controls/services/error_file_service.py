from controls.model.error_file_model import Error_File
from flask import jsonify, make_response
import uuid
from app import db

def get_error_files_service():
    dict_error_files = {}
    try:
        error_files = Error_File.query.all()
        for error_file in error_files:
            dict_error_files[error_file.id]={
                'name':error_file.name,
            }

        return jsonify(dict_error_files)
    except Exception as e:
        return make_response({'message' : str(e)}, 404)