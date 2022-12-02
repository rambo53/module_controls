from app import db

class Method(db.Model) :

    __tablename__ = "method"
    id = db.Column(db.Integer, primary_key=True)
    public_name = db.Column(db.String(50), unique=True, nullable=False)
    method_name = db.Column(db.String(100), unique=True, nullable=False)
    details = db.Column(db.String(200))
    id_public = db.Column(db.String(100), unique=True, nullable=False)
    need_args = db.Column(db.Boolean(), nullable=False)
    created_at = db.Column(db.String(50), nullable=False)
    updated_at = db.Column(db.String(50))
    id_user_create = db.Column(db.Integer, nullable=False)
    id_user_update = db.Column(db.Integer)