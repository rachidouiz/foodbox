import os
import requests
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify

app = Flask(__name__)
app.secret_key = os.getenv("FRONTEND_SECRET", "changeme123")  

# Endpoints des microservices via variables d'environnement
MENU_SVC = os.getenv("MENU_SVC", "http://menu:5001")
COMMANDES_SVC = os.getenv("COMMANDES_SVC", "http://commandes:5003")

# Helpers
def recuperer_menu(nom_menu):
    try:
        resp = requests.get(f"{MENU_SVC}/plats", timeout=3)
        resp.raise_for_status()
        plats = resp.json()
    except Exception as e:
        app.logger.error("Erreur récupération menu: %s", e)
        return {}

    # Filtrer selon nom_menu en reproduisant la logique originale
    menu = {}
    for plat in plats:
        cat = plat.get("categorie", "")
        if nom_menu == "dejeuner" and cat in ["Breuvage matin", "Plats du matin"]:
            menu.setdefault(cat, []).append(plat)
        elif nom_menu == "diner_souper" and cat in ["Breuvages", "Entrées", "Plats principaux", "Desserts"]:
            menu.setdefault(cat, []).append(plat)
    return menu

def calculer_total(panier):
    return sum(item["prix"] * item["quantite"] for item in panier)

# Routes frontend
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu/<nom_menu>', methods=['GET', 'POST'])
def menu(nom_menu):
    if 'panier' not in session:
        session['panier'] = []

    if request.method == 'POST':
        plat_id = request.form.get('plat_id')
        nom = request.form.get('plat_nom')
        prix = float(request.form.get('plat_prix', 0))
        # ajouter au panier local
        panier = session['panier']
        for item in panier:
            if item['nom'] == nom and item['prix'] == prix:
                item['quantite'] += 1
                break
        else:
            panier.append({'nom': nom, 'prix': prix, 'quantite': 1, 'id': plat_id})
        session['panier'] = panier
        session.modified = True
        return redirect(url_for('menu', nom_menu=nom_menu))

    titre = "Menu Déjeuner" if nom_menu == "dejeuner" else "Menu Dîner / Souper"
    menu_data = recuperer_menu(nom_menu)
    total = calculer_total(session.get('panier', []))
    return render_template('menu.html', menu=menu_data, titre_page=titre, panier=session.get('panier', []), total=total)

@app.route('/panier')
def panier():
    panier = session.get('panier', [])
    total = calculer_total(panier)
    return render_template('panier.html', panier=panier, total=total)

@app.route('/ajouter/<int:index>')
def ajouter(index):
    panier = session.get('panier', [])
    if 0 <= index < len(panier):
        panier[index]['quantite'] += 1
        session['panier'] = panier
        session.modified = True
    return redirect(url_for('panier'))

@app.route('/retirer/<int:index>')
def retirer(index):
    panier = session.get('panier', [])
    if 0 <= index < len(panier):
        panier[index]['quantite'] -= 1
        if panier[index]['quantite'] <= 0:
            panier.pop(index)
        session['panier'] = panier
        session.modified = True
    return redirect(url_for('panier'))

@app.route('/vider')
def vider():
    session['panier'] = []
    return redirect(url_for('panier'))

@app.route('/commande', methods=['GET', 'POST'])
def commande():
    panier = session.get('panier', [])
    total = calculer_total(panier)
    if request.method == 'POST':
        nom = request.form.get('nom')
        email = request.form.get('email')
        chambre = request.form.get('chambre')
        instructions = request.form.get('instructions', "")

        # Construire payload pour microservice commandes
        articles = []
        for item in panier:
            articles.append({
                "nom_plat": item['nom'],
                "quantite": item['quantite'],
                "prix": item['prix']
            })
        payload = {
            "nom": nom,
            "numero_chambre": chambre,
            "articles": articles,
            "instructions": instructions
        }
        try:
            resp = requests.post(f"{COMMANDES_SVC}/commandes", json=payload, timeout=5)
            resp.raise_for_status()
        except Exception as e:
            app.logger.error("Erreur création commande: %s", e)
            flash("Impossible d'envoyer la commande pour l'instant. Réessaye plus tard.", "error")
            return redirect(url_for('commande'))

        # vider panier local
        session['panier'] = []
        return render_template('confirmation.html', nom=nom, chambre=chambre)
    return render_template('commande.html', panier=panier, total=total)

# Health-check simple
@app.route('/health')
def health():
    return jsonify({"status": "ok", "services": {"menu": MENU_SVC, "commandes": COMMANDES_SVC}}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
