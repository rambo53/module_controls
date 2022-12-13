from flask import jsonify

def get_pdf_service(data):
    
    try:
        return jsonify({'message' : "ok pour générer pdf", 'status': 200})
    except Exception as e:
        return jsonify({'message' : str(e), 'status':404})