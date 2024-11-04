from .. import db


class StudentValidation(db.Model):
    std_val_id = db.Column(db.Integer, primary_key=True)
    std_id = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)


class AdminValidation(db.Model):
    admin_val_id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)