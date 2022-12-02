from app import db

class Data_File(db.Model) :

    association_table = db.Table('asso_id_data_file_id_configuration', 
        db.Model.metadata,
        db.Column('id_data_file', db.Integer, db.ForeignKey('data_file.id')),
        db.Column('id_config', db.Integer, db.ForeignKey('config.id'))
    )

    __tablename__ = "data_file"
    id = db.Column(db.Integer, primary_key=True)
    id_public = db.Column(db.String(100), unique=True, nullable=False)
    file_name = db.Column(db.String(100), unique=True, nullable=False)
    file_extension = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.String(50), nullable=False)
    updated_at = db.Column(db.String(50))
    id_user_create = db.Column(db.Integer, nullable=False)
    id_user_update = db.Column(db.Integer)

    configs = db.relationship('Config', secondary=association_table, backref="data_file")