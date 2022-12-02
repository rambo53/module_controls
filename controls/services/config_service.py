from controls.model.config_model import Config
from flask import jsonify, make_response
import uuid
from app import db

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