import os
from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from models import db, Commande, ArticleCommande
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
import logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logging.info("Service démarré")
app = Flask(__name__)

# Détection de l'environnement et configuration du chemin de la base
if os.environ.get("FLASK_ENV") == "docker":
    db_path = '/data/commandes.db'
else:
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, '..', 'data', 'commandes.db')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
ma = Marshmallow(app)

# Schémas
class ArticleCommandeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ArticleCommande
        load_instance = True

class CommandeSchema(SQLAlchemyAutoSchema):
    articles = ma.Nested(ArticleCommandeSchema, many=True, attribute="plats")

    class Meta:
        model = Commande
        load_instance = True

commande_schema = CommandeSchema()
commandes_schema = CommandeSchema(many=True)

# Routes
@app.route('/commandes', methods=['POST'])
def creer_commande():
    data = request.json
    commande = Commande(
        nom_client=data['nom'],
        numero_chambre=data['numero_chambre']
    )
    for item in data['articles']:
        article = ArticleCommande(
            nom_plat=item['nom_plat'],
            quantite=item['quantite'],
            prix=item['prix'],
            commande=commande
        )
        db.session.add(article)
    db.session.add(commande)
    db.session.commit()
    return jsonify(commande_schema.dump(commande)), 201

@app.route('/commandes', methods=['GET'])
def lister_commandes():
    commandes = Commande.query.all()
    return jsonify(commandes_schema.dump(commandes))

@app.route('/commandes/<int:id>', methods=['DELETE'])
def supprimer_commande(id):
    commande = Commande.query.get_or_404(id)
    db.session.delete(commande)
    db.session.commit()
    return jsonify({"message": "Commande supprimée"}), 200

################


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", debug=True, port=5003)
