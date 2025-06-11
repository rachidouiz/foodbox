from models import db, Plat
from app import app

plats_demo = [
    # Déjeuner - Breuvage matin
    Plat(nom="Café filtre, décaféiné, thé et infusion", prix=3.50, categorie="Breuvage matin"),
    Plat(nom="Café expresso", prix=4.00, categorie="Breuvage matin"),
    Plat(nom="Café allongé", prix=4.75, categorie="Breuvage matin"),
    Plat(nom="Café au lait ou Mokaccino", prix=5.00, categorie="Breuvage matin"),
    Plat(nom="Bol de café au lait", prix=5.75, categorie="Breuvage matin"),
    Plat(nom="Cappuccino", prix=4.50, categorie="Breuvage matin"),
    Plat(nom="Jus d’orange ou de pamplemousse fraîchement pressé", prix=6.00, categorie="Breuvage matin"),
    Plat(nom="Jus (orange, pomme, raisin, pamplemousse, canneberge)", prix=3.00, categorie="Breuvage matin"),
    Plat(nom="Chocolat chaud ou froid ou lait", prix=3.50, categorie="Breuvage matin"),

    # Déjeuner - Plats du matin
    Plat(nom="Le déjeuner un œuf", prix=11.00, categorie="Plats du matin"),
    Plat(nom="Le déjeuner deux œufs", prix=12.00, categorie="Plats du matin"),
    Plat(nom="Le déjeuner un œuf, bacon/jambon/saucisse", prix=14.00, categorie="Plats du matin"),
    Plat(nom="Le déjeuner deux œufs, bacon/jambon/saucisse", prix=15.00, categorie="Plats du matin"),
    Plat(nom="Muffin du jour et café", prix=8.00, categorie="Plats du matin"),
    Plat(nom="Bol de céréales avec lait", prix=7.00, categorie="Plats du matin"),
    Plat(nom="L’hermitage (Yogourt, fruits, céréales)", prix=11.00, categorie="Plats du matin"),
    Plat(nom="Gruau avec fruits", prix=11.00, categorie="Plats du matin"),
    Plat(nom="Assiette de fruits du marché et fromage cottage", prix=11.00, categorie="Plats du matin"),
    Plat(nom="Armand le coureur des bois", prix=11.00, categorie="Plats du matin"),
    Plat(nom="Réveil sur le fjord", prix=12.00, categorie="Plats du matin"),
    Plat(nom="Le zoo", prix=19.50, categorie="Plats du matin"),
    Plat(nom="Bagel au fromage", prix=10.00, categorie="Plats du matin"),
    Plat(nom="Croissant garni Légendaire", prix=15.00, categorie="Plats du matin"),

    # Diner/souper - Breuvages (exemples, à compléter selon tes besoins)
    Plat(nom="CÉSAR CLASSIQUE", prix=10.00, categorie="Breuvages"),
    Plat(nom="LE FJORD", prix=11.00, categorie="Breuvages"),
    Plat(nom="MOJITO BLEUET", prix=11.00, categorie="Breuvages"),
    Plat(nom="ST-TROPEZ (sans alcool)", prix=8.00, categorie="Breuvages"),
    Plat(nom="BUDWEISER 16 oz", prix=9.00, categorie="Breuvages"),

    # Diner/souper - Entrées
    Plat(nom="Potage du moment", prix=5.00, categorie="Entrées"),
    Plat(nom="Salade du marché", prix=8.00, categorie="Entrées"),
    Plat(nom="Escargots à l’ail", prix=9.00, categorie="Entrées"),
    Plat(nom="Cornichons frits", prix=10.00, categorie="Entrées"),
    Plat(nom="Salade César", prix=12.00, categorie="Entrées"),
    Plat(nom="Soupe à l’oignon gratinée", prix=11.00, categorie="Entrées"),
    Plat(nom="Ailes de poulet (8)", prix=15.00, categorie="Entrées"),

    # Diner/souper - Plats principaux
    Plat(nom="Spaghetti sauce à la viande du Légendaire", prix=20.00, categorie="Plats principaux"),
    Plat(nom="Carbonara moderne", prix=25.00, categorie="Plats principaux"),
    Plat(nom="Linguine aux fruits de mer", prix=37.00, categorie="Plats principaux"),
    Plat(nom="Burger de bœuf", prix=23.00, categorie="Plats principaux"),
    Plat(nom="Brochette de poulet mariné", prix=30.00, categorie="Plats principaux"),
    Plat(nom="Filet mignon de bœuf AAA 6 oz", prix=45.00, categorie="Plats principaux"),

    # Diner/souper - Desserts
    Plat(nom="Gâteau mi-cuit au chocolat", prix=7.00, categorie="Desserts"),
    Plat(nom="Gâteau au fromage et caramel salé", prix=7.00, categorie="Desserts"),
    Plat(nom="Baladin de mousse aux trois chocolats", prix=7.00, categorie="Desserts"),
    Plat(nom="Crème brûlée maison", prix=7.00, categorie="Desserts"),
]

with app.app_context():
    db.create_all()
    db.session.add_all(plats_demo)
    db.session.commit()
    print("Tous les plats sont ajoutés à la base de données.")