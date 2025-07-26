from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(120), nullable=False)
    prix = db.Column(db.Float, nullable=False)
    categorie = db.Column(db.String(80), nullable=False)
