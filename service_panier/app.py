from flask import Flask, jsonify, request
from panier_utils import ajouter_au_panier, retirer_du_panier, calculer_total

app = Flask(__name__)

# Panier temporaire en mémoire (non persistant)
panier = []

@app.route('/panier', methods=['GET'])
def get_panier():
    return jsonify(panier), 200

@app.route('/panier', methods=['POST'])
def ajouter_item():
    data = request.json
    if not data or 'nom' not in data or 'prix' not in data:
        return jsonify({'error': 'Nom et prix requis'}), 400

    item_id = len(panier) + 1
    item = {
        'id': item_id,
        'nom': data['nom'],
        'prix': data['prix']
    }
    ajouter_au_panier(panier, item)
    return jsonify(item), 201

@app.route('/panier/<int:item_id>', methods=['DELETE'])
def supprimer_item(item_id):
    global panier
    panier = retirer_du_panier(panier, item_id)
    return jsonify({'message': f'Item {item_id} supprimé'}), 200

@app.route('/panier/total', methods=['GET'])
def get_total():
    total = calculer_total(panier)
    return jsonify({'total': total}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5002)
