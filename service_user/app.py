from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Utilisateur  # on importe le modèle correct
import os

app = Flask(__name__)

# Pour détecter si on est dans Docker (où /data est monté)
if os.environ.get("FLASK_ENV") == "docker":
    db_path = '/data/users.db'
else:
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, '..', 'data', 'users.db')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # initialise SQLAlchemy avec l'app

# --- INSCRIPTION ---
@app.route('/auth/inscription', methods=['POST'])
def inscription():
    data = request.get_json()
    if Utilisateur.query.filter_by(nom_utilisateur=data['nom_utilisateur']).first():
        return jsonify({"message": "Utilisateur déjà existant"}), 400

    hash_pwd = generate_password_hash(data['mot_de_passe'])
    role = data.get('role', 'admin')  # par défaut admin

    nouvel_utilisateur = Utilisateur(
        nom_utilisateur=data['nom_utilisateur'],
        mot_de_passe_hash=hash_pwd,
        role=role
    )
    db.session.add(nouvel_utilisateur)
    db.session.commit()
    return jsonify({"message": "Utilisateur inscrit avec succès"}), 201

# --- CONNEXION ---
@app.route('/auth/connexion', methods=['POST'])
def connexion():
    data = request.get_json()
    utilisateur = Utilisateur.query.filter_by(nom_utilisateur=data['nom_utilisateur']).first()
    if utilisateur and check_password_hash(utilisateur.mot_de_passe_hash, data['mot_de_passe']):
        return jsonify({
            "message": "Connexion réussie",
            "role": utilisateur.role,
            "utilisateur": utilisateur.nom_utilisateur
        }), 200
    return jsonify({"message": "Nom d'utilisateur ou mot de passe incorrect"}), 401

# --- MAIN ---
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", debug=True, port=5004)
