from controls.model.data_file_model import Data_File
from controls.utils.directory_utils import create_directory, get_file_extension, get_filename
from controls.utils.date_utils import get_datetime
from controls.utils.fake_data_utils import get_fake_id_user
from controls.utils.df_utils import Df_Utils
from flask import jsonify
import uuid
from app import db
import sys

def get_data_files_service():
    try:
        data_files = Data_File.query.all()
        list_data_files = []

        for data_file in data_files:

            lst_configs = data_file.configs.all()
            configs = []
            
            if len(lst_configs) > 0:

                for config in lst_configs:
                    new_dict_config = {
                        'id':config.id_public,
                        'name':config.name,
                        'config_user_create':config.user.name,
                    }
                    configs.append(new_dict_config)
            
            new_dict_data_file = {
                'id':data_file.id_public,
                'user_name': data_file.user.name,
                'file_name':data_file.file_name,
                'configs': configs
            }

            list_data_files.append(new_dict_data_file)
        
        return jsonify(list_data_files)
    except Exception as e:
        return jsonify({'message' : str(e), "status":404})


def get_data_file_service(id_public):
    try:
        data_file = Data_File.query.filter(Data_File.id_public==id_public).first_or_404()
        model = {
            'id': data_file.id_public,
            'name': data_file.file_name,
            'nb_rows': data_file.nb_rows,
            'nb_cols':data_file.nb_cols,
            'first_rows':data_file.first_rows,
        }
        return jsonify(model)
    except Exception as e:
        return jsonify({'message' : str(e), "status":404})


def add_data_files_service(new_file):
    try:
        data_file_path = create_directory(new_file)

        df_from_data = Df_Utils(data_file_path)

        data_file = Data_File()
        data_file.id_public = str(uuid.uuid4())
        data_file.file_name = get_filename(new_file.filename)
        data_file.file_extension = get_file_extension(new_file.filename)
        data_file.created_at = get_datetime()
        data_file.nb_rows = df_from_data.nb_rows
        data_file.nb_cols = df_from_data.nb_cols
        data_file.first_rows = df_from_data.first_rows

        # TODO update when loggin user ok
        data_file.id_user_create = get_fake_id_user()

        db.session.add(data_file)
        db.session.commit()
    except Exception as e:
        return jsonify({'message' : str(e), 'status': 404})

    model = {'message' : "c'est ok", 'status': 200}
    return jsonify(model)

    
