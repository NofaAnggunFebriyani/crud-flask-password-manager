from app import db

class Tambah(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Platform = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(100), nullable=False)
    Password = db.Column(db.String(100), nullable=False)