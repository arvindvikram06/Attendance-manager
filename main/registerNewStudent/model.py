from .. import db


class StudentDetails(db.Model):
    std_id = db.Column(db.Integer, primary_key=True)
    lab_code = db.Column(db.Integer, nullable=False)
    std_name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    roll_num = db.Column(db.String(50), unique=True, nullable=False)
    dept = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    face_reg_status = db.Column(db.Boolean, default=False, nullable=False)
    reg_date = db.Column(db.String(20), nullable=False)


