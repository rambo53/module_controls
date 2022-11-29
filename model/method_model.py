from app import db

class Method(db.Model) :

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    method_name = db.Column(db.String(100), unique=True, nullable=False)
    details = db.Column(db.String(200))
    number_of_args = db.Column(db.Integer(), nullable=False)