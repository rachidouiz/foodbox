from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Utilisateur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom_utilisateur = db.Column(db.String(80), unique=True, nullable=False)
    mot_de_passe_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="admin")  
