from models import Plat
from collections import defaultdict

def get_menu_by_name(nom_menu):
    plats = Plat.query.all()
    menu = defaultdict(list)

    for plat in plats:
        if nom_menu == 'dejeuner' and plat.categorie in ['Breuvage matin', 'Plats du matin']:
            menu[plat.categorie].append({'nom': plat.nom, 'prix': plat.prix})
        elif nom_menu == 'diner_souper' and plat.categorie in ['Breuvages', 'Entrées', 'Plats principaux', 'Desserts']:
            menu[plat.categorie].append({'nom': plat.nom, 'prix': plat.prix})

    return dict(menu)

def ajouter_au_panier(panier, plat_nom, plat_prix):
    for item in panier:
        if item['nom'] == plat_nom and item['prix'] == plat_prix:
            item['quantite'] += 1
            break
    else:
        panier.append({'nom': plat_nom, 'prix': plat_prix, 'quantite': 1})
    return panier

def retirer_du_panier(panier, index):
    if 0 <= index < len(panier):
        panier[index]['quantite'] -= 1
        if panier[index]['quantite'] <= 0:
            panier.pop(index)
    return panier

def calculer_total(panier):
    return sum(plat['prix'] * plat['quantite'] for plat in panier)
