from app import db


class PdfTemplate(db.Model) :
    
    __tablename__ = "pdf_template"
    id = db.Column(db.Integer, primary_key=True)
    id_public = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)