from controls.model.data_file_model import Data_File
from controls.utils.directory_utils import create_directory, get_file_extension, get_filename
from controls.utils.date_utils import get_datetime, format_datetime
from controls.utils.fake_data_utils import get_fake_id_user
from flask import jsonify
import uuid
from app import db

def get_data_files_service():
    dict_data_files = []
    try:
        data_files = Data_File.query.all()
        dict_data_files = []
        for data_file in data_files:

            lst_config = []

            if len(data_file.configs) > 0:

                for config in data_file.configs:
                    new_dict_config = {
                        'config_name':config.name,
                        'config_user_create':config.user.name,
                    }
                    lst_config.append(new_dict_config)
            
            new_dict_data_file = {
                'id':data_file.id_public,
                'user_name': data_file.user.name,
                'file_name':data_file.file_name,
                'configs': lst_config
            }

            dict_data_files.append(new_dict_data_file)
            '''
            dict_data_files[data_file.id_public]={
                'user_name': data_file.user.name,
                'public_id': data_file.id_public,
                'file_name':data_file.file_name,
            }
            if len(data_file.configs) > 0:
                dict_data_files[data_file.id_public]['configs'] = {}
                for config in data_file.configs:
                    dict_data_files[data_file.id_public]['configs'][config.id_public] = {
                        'config_name':config.name,
                        'config_user_create':config.user.name,
                        #'config_create':format_datetime(config.created_at)
                    }
            '''
        return jsonify(dict_data_files)
    except Exception as e:
        return jsonify({'message' : str(e), "status":404})


def add_data_files_service(new_file):
    try:
        create_directory(new_file)

        data_file = Data_File()
        data_file.id_public = str(uuid.uuid4())
        data_file.file_name = get_filename(new_file.filename)
        data_file.file_extension = get_file_extension(new_file.filename)
        data_file.created_at = get_datetime()

        # TODO update when loggin user ok
        data_file.id_user_create = get_fake_id_user()

        db.session.add(data_file)
        db.session.commit()
    except Exception as e:
        return jsonify({'message' : str(e), 'status': 404})

    model = {'message' : "c'est ok", 'status': 200}
    return jsonify(model)

    
