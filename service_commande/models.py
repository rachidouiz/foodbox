from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Commande(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom_client = db.Column(db.String(120), nullable=False)
    numero_chambre = db.Column(db.String(10), nullable=False)
    plats = db.relationship('ArticleCommande', backref='commande', cascade="all, delete")

class ArticleCommande(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom_plat = db.Column(db.String(120), nullable=False)
    quantite = db.Column(db.Integer, nullable=False)
    prix = db.Column(db.Float, nullable=False)
    commande_id = db.Column(db.Integer, db.ForeignKey('commande.id'))
