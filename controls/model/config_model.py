from app import db
from user_model import User

class Config(db.Model) :

    __tablename__ = "config"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    config_dict = db.Column(db.String(2000), nullable=False)
    id_public = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.String(50), nullable=False)
    updated_at = db.Column(db.String(50))
    id_user_create = db.Column(db.Integer, db.ForeignKey("user.id"))
    id_user_update = db.Column(db.Integer)

    user = db.relationship(User, back_populates="configs")


    
