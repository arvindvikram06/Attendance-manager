from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set the secret key
app.secret_key = 'this_is_a_secretkey'
# Setting up DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendanceManager.db'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

# Linking the pages
from .attendance import routes
from .registerNewStudent import routes
from .validation import routes