from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Interger, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)