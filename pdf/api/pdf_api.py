from flask import Blueprint, request
from pdf.services.pdf_services import get_pdf_service
pdf_route = Blueprint('pdf', __name__)

@pdf_route.route("/generate_pdf", methods=['POST'])
def generate_pdf():
    data = request.get_json()
    return get_pdf_service(data)