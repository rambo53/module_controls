from app import db

class User(db.Model) :

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
    data_files = db.relationship("Data_File", back_populates="user")
    configs = db.relationship("Config", back_populates="user")
