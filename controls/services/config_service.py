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


def get_config_service(id_public):
    try:
        config = Config.query.filter(Config.id_public==id_public).first_or_404()
        model = {
            'name': config.name
        }
        return jsonify(model)
    except Exception as e:
        return jsonify({'message' : str(e), "status":404})
