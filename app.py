from flask import Flask, render_template, request, redirect, url_for, session
from services import get_menu_by_name, ajouter_au_panier, retirer_du_panier, calculer_total

app = Flask(__name__)
app.secret_key = 'secret123'  # Pour la session panier

# Page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Page de menu
@app.route('/menu/<nom_menu>', methods=['GET', 'POST'])
def menu(nom_menu: str):
    if 'panier' not in session:
        session['panier'] = []

    menu = get_menu_by_name(nom_menu)
    if not menu:
        return "Menu introuvable", 404

    if request.method == 'POST':
        plat_nom = request.form.get('plat_nom')
        plat_prix_str = request.form.get('plat_prix')
        if plat_nom is None or plat_prix_str is None:
            return "Erreur : Données manquantes", 400
        try:
            plat_prix = float(plat_prix_str)
        except ValueError:
            return "Erreur : Prix invalide", 400

        session['panier'] = ajouter_au_panier(session['panier'], plat_nom, plat_prix)
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
    app.run(debug=True)
