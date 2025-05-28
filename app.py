from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret123'  # Pour la session panier

menus = {
    "dejeuner": {
        "Breuvage matin": [
            {"nom": "Café filtre, décaféiné, thé et infusion", "prix": 3.50},
            {"nom": "Café expresso", "prix": 4.00},
            {"nom": "Café allongé", "prix": 4.75},
            {"nom": "Café au lait ou Mokaccino", "prix": 5.00},
            {"nom": "Bol de café au lait", "prix": 5.75},
            {"nom": "Cappuccino", "prix": 4.50},
            {"nom": "Jus d’orange ou de pamplemousse fraîchement pressé", "prix": 6.00},
            {"nom": "Jus (orange, pomme, raisin, pamplemousse, canneberge)", "prix": 3.00},
            {"nom": "Chocolat chaud ou froid ou lait", "prix": 3.50},
        ],
        "Plats du matin": [
            {"nom": "Le déjeuner un œuf", "prix": 11.00},
            {"nom": "Le déjeuner deux œufs", "prix": 12.00},
            {"nom": "Le déjeuner un œuf, bacon/jambon/saucisse", "prix": 14.00},
            {"nom": "Le déjeuner deux œufs, bacon/jambon/saucisse", "prix": 15.00},
            {"nom": "Muffin du jour et café", "prix": 8.00},
            {"nom": "Bol de céréales avec lait", "prix": 7.00},
            {"nom": "L’hermitage (Yogourt, fruits, céréales)", "prix": 11.00},
            {"nom": "Gruau avec fruits", "prix": 11.00},
            {"nom": "Assiette de fruits du marché et fromage cottage", "prix": 11.00},
            {"nom": "Armand le coureur des bois", "prix": 11.00},
            {"nom": "Réveil sur le fjord", "prix": 12.00},
            {"nom": "Le zoo", "prix": 19.50},
            {"nom": "Bagel au fromage", "prix": 10.00},
            {"nom": "Croissant garni Légendaire", "prix": 15.00},
        ],
    },
    "diner_souper": {
        "Breuvages": [
            {"nom": "CÉSAR CLASSIQUE", "prix": 10.00},
            {"nom": "LE FJORD", "prix": 11.00},
            {"nom": "MOJITO BLEUET", "prix": 11.00},
            {"nom": "ST-TROPEZ (sans alcool)", "prix": 8.00},
            {"nom": "BUDWEISER 16 oz", "prix": 9.00},
            # ... 
        ],
        "Entrées": [
            {"nom": "Potage du moment", "prix": 5.00},
            {"nom": "Salade du marché", "prix": 8.00},
            {"nom": "Escargots à l’ail", "prix": 9.00},
            {"nom": "Cornichons frits", "prix": 10.00},
            {"nom": "Salade César", "prix": 12.00},
            {"nom": "Soupe à l’oignon gratinée", "prix": 11.00},
            {"nom": "Ailes de poulet (8)", "prix": 15.00},
            # ...
        ],
        "Plats principaux": [
            {"nom": "Spaghetti sauce à la viande du Légendaire", "prix": 20.00},
            {"nom": "Carbonara moderne", "prix": 25.00},
            {"nom": "Linguine aux fruits de mer", "prix": 37.00},
            {"nom": "Burger de bœuf", "prix": 23.00},
            {"nom": "Brochette de poulet mariné", "prix": 30.00},
            {"nom": "Filet mignon de bœuf AAA 6 oz", "prix": 45.00},
            # ...
        ],
        "Desserts": [
            {"nom": "Gâteau mi-cuit au chocolat", "prix": 7.00},
            {"nom": "Gâteau au fromage et caramel salé", "prix": 7.00},
            {"nom": "Baladin de mousse aux trois chocolats", "prix": 7.00},
            {"nom": "Crème brûlée maison", "prix": 7.00},
        ],
    }
}

# Page d'accueil : 
@app.route('/')
def index():
    return render_template('index.html')
# Page de menu :
@app.route('/menu/<nom_menu>', methods=['GET', 'POST'])
def menu(nom_menu):
    if 'panier' not in session:
        session['panier'] = []

    menu = menus.get(nom_menu)
    if not menu:
        return "Menu introuvable", 404

    if request.method == 'POST':
        plat_nom = request.form.get('plat_nom')
        plat_prix = float(request.form.get('plat_prix') or 0)

        panier = session['panier']
        for item in panier:
            if item['nom'] == plat_nom and item['prix'] == plat_prix:
                item['quantite'] += 1
                break
        else:
            panier.append({'nom': plat_nom, 'prix': plat_prix, 'quantite': 1})

        session['panier'] = panier
        session.modified = True
        return redirect(url_for('menu', nom_menu=nom_menu))

    titre = "Menu Déjeuner" if nom_menu == "dejeuner" else "Menu Dîner / Souper"
    return render_template(
        'menu.html',
        menu=menu,
        titre_page=titre,
        panier=session['panier']
    )


# Page du panier
@app.route('/panier')
def panier():
    panier = session.get('panier', [])
    total = sum(plat['prix'] * plat['quantite'] for plat in panier)
    return render_template('panier.html', panier=panier, total=total)

# Vider le panier
@app.route('/vider')
def vider():
    session['panier'] = []
    return redirect(url_for('panier'))
@app.route('/ajouter/<int:index>')
def ajouter(index):
    if 'panier' in session and 0 <= index < len(session['panier']):
        session['panier'][index]['quantite'] += 1
        session.modified = True
    return redirect(url_for('panier'))

@app.route('/retirer/<int:index>')
def retirer(index):
    if 'panier' in session and 0 <= index < len(session['panier']):
        session['panier'][index]['quantite'] -= 1
        if session['panier'][index]['quantite'] <= 0:
            session['panier'].pop(index)
        session.modified = True
    return redirect(url_for('panier'))

@app.route('/commande', methods=['GET', 'POST'])
def commande():
    panier = session.get('panier', [])
    total = sum(plat['prix'] * plat['quantite'] for plat in panier)
    if request.method == 'POST':
        nom = request.form.get('nom')
        email = request.form.get('email')
        chambre = request.form.get('chambre')
        instructions = request.form.get('instructions')
        # Ici on stocker la commande
        session['panier'] = []
        return render_template('confirmation.html', nom=nom, chambre=chambre)
    return render_template('commande.html', panier=panier, total=total)



if __name__ == '__main__':
    app.run(debug=True)
