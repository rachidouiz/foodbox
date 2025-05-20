from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret123'  # Pour la session panier

# Simuler la "base de données" des plats
PLATS = [
    {"id": 1, "nom": "Pizza Margherita", "prix": 10.99},
    {"id": 2, "nom": "Burger classique", "prix": 8.50},
    {"id": 3, "nom": "Salade César", "prix": 7.00},
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
