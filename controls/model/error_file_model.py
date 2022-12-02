from app import db

class Error_File(db.Model) :

    __tablename__ = "error_file"
    id = db.Column(db.Integer, primary_key=True)
    id_public = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    id_data_file = db.Column(db.Integer, nullable=False)
    id_configuration = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.String(50), nullable=False)
    updated_at = db.Column(db.String(50))
    id_user_create = db.Column(db.Integer, nullable=False)
    id_user_create = db.Column(db.Integer, nullable=False)