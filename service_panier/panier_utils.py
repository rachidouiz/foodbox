def ajouter_au_panier(panier, item):
    panier.append(item)
    return panier

def retirer_du_panier(panier, item_id):
    return [item for item in panier if item['id'] != item_id]

def calculer_total(panier):
    return round(sum(item['prix'] for item in panier), 2)
