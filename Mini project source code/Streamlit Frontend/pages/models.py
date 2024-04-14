from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    name = db.Column(db.String(20), primary_key=True)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password