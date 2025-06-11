from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(120), nullable=False)
    prix = db.Column(db.Float, nullable=False)
    categorie = db.Column(db.String(80), nullable=False)

class Commande(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom_client = db.Column(db.String(100))
    email = db.Column(db.String(120))
    chambre = db.Column(db.String(10))
    instructions = db.Column(db.Text)
    date_commande = db.Column(db.DateTime, server_default=db.func.now())
    articles = db.relationship('ArticleCommande', backref='commande', lazy=True)

class ArticleCommande(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    commande_id = db.Column(db.Integer, db.ForeignKey('commande.id'))
    plat_id = db.Column(db.Integer, db.ForeignKey('plat.id'))
    quantite = db.Column(db.Integer)
    plat = db.relationship('Plat')
