from controls.model.config_model import Config
from controls.model.data_file_model import Data_File
from flask import jsonify, make_response
from controls.utils.fake_data_utils import get_fake_name_config, get_fake_id_user
from controls.utils.date_utils import get_datetime
import uuid
from app import db
import ast
import sys

def get_configs_service():
    dict_configs = {}
    try:
        configs = Config.query.all()
        for config in configs:
            dict_configs[config.id]={
                'name':config.name,
            }

        return jsonify(dict_configs)
    except Exception as e:
        return make_response({'message' : str(e)}, 404)


def get_config_service(id_public):
    try:
        config = Config.query.filter(Config.id_public==id_public).first_or_404()
        model = {
            'name': config.name,
            'config_dict': ast.literal_eval(config.config_dict)
        }
        return jsonify(model)
    except Exception as e:
        return jsonify({'message' : str(e), "status":404})


def add_config_service(data):

    try: 
        new_config = Config()
        data_file_id = Data_File.query.filter(Data_File.id_public==data['id_file']).first_or_404()

        new_config.id_public = str(uuid.uuid4())
        new_config.config_dict = str(data['config'])
        new_config.created_at = get_datetime()

        new_config.name = get_fake_name_config()
        new_config.id_user_create = get_fake_id_user()

        new_config.data_file.append(data_file_id)

        db.session.add(new_config)
        db.session.commit()

        return jsonify({'message' : "ok post config", "status":200})
    except Exception as e:
        return jsonify({'message' : str(e), "status":404})
    
    
def update_config_service(data):
    try:
        config_to_patch = Config.query.filter(Config.id_public==data['id_config']).first_or_404()
        config_to_patch.config_dict = str(data['config'])
        db.session.commit()
        return jsonify({'message' : "ok patch config", "status":200})
    except Exception as e:
        return jsonify({'message' : str(e), "status":404})
