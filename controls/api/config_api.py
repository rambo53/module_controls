from flask import Blueprint, request
from controls.services.config_service import get_configs_service, get_config_service, add_config_service
config_route = Blueprint('config', __name__)

@config_route.route("/configs", methods=['GET'])
def get_configs():
    return get_configs_service()

@config_route.route("/config/<id_public>", methods=['GET'])
def get_config(id_public):
    return get_config_service(id_public)

@config_route.route("/config", methods=['POST'])
def add_method():
    data = request.get_json()
    return add_config_service(data)
