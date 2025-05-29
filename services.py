from data import get_menus

def get_menu_by_name(nom_menu):
    menus = get_menus()
    return menus.get(nom_menu)

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
