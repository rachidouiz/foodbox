from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret123'  # Pour la session panier

# Simuler la "base de données" des plats
PLATS = [
    {"id": 1, "nom": "Poutine Légendaire", "prix": 12.99},
    {"id": 2, "nom": "Burger du Chef (bœuf AAA, fromage Perron, bacon, frites)", "prix": 23.00},
    {"id": 3, "nom": "Spaghetti sauce à la viande du Légendaire", "prix": 20.00},
    {"id": 4, "nom": "Brochette de poulet mariné", "prix": 30.00},
    {"id": 5, "nom": "Fish and Chips maison", "prix": 29.00},
    {"id": 6, "nom": "Tartare de saumon, fraises et lime", "prix": 32.00},
    {"id": 7, "nom": "Salade méchouia Tunisienne", "prix": 12.00},
    {"id": 8, "nom": "Carbonara moderne (Linguine, pancetta, parmesan)", "prix": 25.00},
    {"id": 9, "nom": "Crêpe maison ou pain doré", "prix": 14.00},
    {"id": 10, "nom": "Gâteau mi-cuit au chocolat", "prix": 7.00},
]

# Page d'accueil : affiche plats + formulaire d'ajout
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'panier' not in session:
        session['panier'] = []

    # Ajouter un plat au panier
    if request.method == 'POST':
        plat_id = int(request.form.get('plat_id'))
        for plat in PLATS:
            if plat['id'] == plat_id:
                session['panier'].append(plat)
                session.modified = True
                break
        return redirect(url_for('index'))

    return render_template('index.html', plats=PLATS, panier=session['panier'])

# Page du panier
@app.route('/panier')
def panier():
    panier = session.get('panier', [])
    total = sum(plat['prix'] for plat in panier)
    return render_template('panier.html', panier=panier, total=total)

# Vider le panier
@app.route('/vider')
def vider():
    session['panier'] = []
    return redirect(url_for('panier'))

if __name__ == '__main__':
    app.run(debug=True)
