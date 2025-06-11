from flask import Flask, render_template, request, redirect, url_for, session
from services import ajouter_au_panier, retirer_du_panier, calculer_total
from models import db, Plat
from collections import defaultdict


app = Flask(__name__)
app.secret_key = 'secret123'  # Pour la session panier

# --- CONFIGURATION SQLALCHEMY ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foodbox.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Page de menu
@app.route('/menu/<nom_menu>', methods=['GET', 'POST'])
def menu(nom_menu):
    if 'panier' not in session:
        session['panier'] = []

    # Lecture directe des plats depuis la base
    plats = Plat.query.all()
    menu = defaultdict(list)

    for plat in plats:
        if nom_menu == 'dejeuner' and plat.categorie in ['Breuvage matin', 'Plats du matin']:
            menu[plat.categorie].append(plat)
        elif nom_menu == 'diner_souper' and plat.categorie in ['Breuvages', 'Entrées', 'Plats principaux', 'Desserts']:
            menu[plat.categorie].append(plat)

    if not menu:
        return "Menu introuvable ou vide", 404

    if request.method == 'POST':
        plat_id_str = request.form.get('plat_id')
        if not plat_id_str:
            return "Erreur : plat_id manquant", 400
        try:
            plat_id = int(plat_id_str)
        except ValueError:
            return "Erreur : plat_id invalide", 400

        plat = Plat.query.get(plat_id)
        if not plat:
            return "Plat introuvable", 404

        panier = session['panier']
        for item in panier:
            if item['nom'] == plat.nom and item['prix'] == plat.prix:
                item['quantite'] += 1
                break
        else:
            panier.append({'nom': plat.nom, 'prix': plat.prix, 'quantite': 1})

        session['panier'] = panier
        session.modified = True
        return redirect(url_for('menu', nom_menu=nom_menu))

    titre = "Menu Déjeuner" if nom_menu == "dejeuner" else "Menu Dîner / Souper"
    return render_template('menu.html', menu=menu, titre_page=titre, panier=session['panier'])
# Page du panier
@app.route('/panier')
def panier():
    panier = session.get('panier', [])
    total = calculer_total(panier)
    return render_template('panier.html', panier=panier, total=total)

# Vider le panier
@app.route('/vider')
def vider():
    session['panier'] = []
    return redirect(url_for('panier'))

@app.route('/ajouter/<int:index>')
def ajouter(index: int):
    if 'panier' in session and 0 <= index < len(session['panier']):
        session['panier'][index]['quantite'] += 1
        session.modified = True
    return redirect(url_for('panier'))

@app.route('/retirer/<int:index>')
def retirer(index: int):
    if 'panier' in session and 0 <= index < len(session['panier']):
        session['panier'] = retirer_du_panier(session['panier'], index)
        session.modified = True
    return redirect(url_for('panier'))

@app.route('/commande', methods=['GET', 'POST'])
def commande():
    panier = session.get('panier', [])
    total = calculer_total(panier)
    if request.method == 'POST':
        nom = request.form.get('nom')
        email = request.form.get('email')
        chambre = request.form.get('chambre')
        instructions = request.form.get('instructions')
        session['panier'] = []
        return render_template('confirmation.html', nom=nom, chambre=chambre)
    return render_template('commande.html', panier=panier, total=total)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
