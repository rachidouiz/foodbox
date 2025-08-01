import os
from flask import Flask, jsonify, request
from models import db, Plat
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

app = Flask(__name__)

# Gestion du chemin vers la base de données (Docker vs local)
if os.environ.get("FLASK_ENV") == "docker":
    db_path = '/data/menu.db'
else:
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, '..', 'data', 'menu.db')

print("DB utilisée :", db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
ma = Marshmallow(app)

# Schéma de sérialisation
class PlatSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Plat
        load_instance = True

plat_schema = PlatSchema()
plats_schema = PlatSchema(many=True)

@app.route('/plats', methods=['GET'])
def get_plats():
    plats = Plat.query.all()
    return jsonify(plats_schema.dump(plats))

@app.route('/plats', methods=['POST'])
def add_plat():
    data = request.json
    nouveau_plat = Plat(
        nom=data['nom'],
        prix=data['prix'],
        categorie=data['categorie']
    )
    db.session.add(nouveau_plat)
    db.session.commit()
    return jsonify(plat_schema.dump(nouveau_plat)), 201

@app.route('/plats/<int:id>', methods=['PUT'])
def update_plat(id):
    plat = Plat.query.get_or_404(id)
    data = request.json
    plat.nom = data.get('nom', plat.nom)
    plat.prix = data.get('prix', plat.prix)
    plat.categorie = data.get('categorie', plat.categorie)
    db.session.commit()
    return jsonify(plat_schema.dump(plat))

@app.route('/plats/<int:id>', methods=['DELETE'])
def delete_plat(id):
    plat = Plat.query.get_or_404(id)
    db.session.delete(plat)
    db.session.commit()
    return jsonify({"message": "Plat supprimé"}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", debug=True, port=5001)
