from flask import Blueprint, request
from pdf.services.data_from_akeneo_service import get_first_rows_service, get_products_service
data_from_akeneo_route = Blueprint('data_from_akeneo', __name__)


@data_from_akeneo_route.route("/get_first_rows", methods=['GET'])
def get_first_rows():
    return get_first_rows_service()

@data_from_akeneo_route.route("/get_products/<search_string>", methods=['GET'])
def get_products(search_string):
    return get_products_service(search_string)