from controls.model.data_file_model import Data_File
from flask import jsonify, make_response
import uuid
from app import db

def get_data_files_service():
    dict_data_files = []
    try:
        data_files = Data_File.query.all()
        for data_file in data_files:
            
            dict_data_files.append({
                'user_name': data_file.user.name,
                'public_id': data_file.id_public,
                'file_name':data_file.file_name,
                'configs': data_file.configs[0].name +" "+ data_file.configs[1].name
            })

        return jsonify(dict_data_files)
    except Exception as e:
        return make_response({'message' : str(e)}, 404)
