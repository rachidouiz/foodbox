from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modèle utilisateur
class Utilisateur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom_utilisateur = db.Column(db.String(80), unique=True, nullable=False)
    mot_de_passe_hash = db.Column(db.String(128), nullable=False)

# Inscription
@app.route('/auth/inscription', methods=['POST'])
def inscription():
    data = request.get_json()
    if Utilisateur.query.filter_by(nom_utilisateur=data['nom_utilisateur']).first():
        return jsonify({"message": "Utilisateur déjà existant"}), 400
    hash_pwd = generate_password_hash(data['mot_de_passe'])
    nouvel_utilisateur = Utilisateur(nom_utilisateur=data['nom_utilisateur'], mot_de_passe_hash=hash_pwd)
    db.session.add(nouvel_utilisateur)
    db.session.commit()
    return jsonify({"message": "Utilisateur inscrit avec succès"}), 201

# Connexion
@app.route('/auth/connexion', methods=['POST'])
def connexion():
    data = request.get_json()
    utilisateur = Utilisateur.query.filter_by(nom_utilisateur=data['nom_utilisateur']).first()
    if utilisateur and check_password_hash(utilisateur.mot_de_passe_hash, data['mot_de_passe']):
        return jsonify({"message": "Connexion réussie"}), 200
    return jsonify({"message": "Nom d'utilisateur ou mot de passe incorrect"}), 401

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5004)
