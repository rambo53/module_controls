from flask import jsonify
import os
from pdf.model.products_model import Products_model

def get_first_rows_service():
    try:
        dict_all_products = Products_model().get_all_products_from_csv()
        dict_products = dict_all_products[:20]
        return jsonify({'products': dict_products, 'status': 200})
    except Exception as e:
        return jsonify({'message' : str(e), 'status':404})


def get_products_service(search_string):
    try:
        dict_all_products = Products_model().get_all_products_from_csv()
        dict_products = dict_all_products[:5]
        return jsonify({'products' : dict_products, 'status': 200})
    except Exception as e:
        return jsonify({'message' : str(e), 'status':404})