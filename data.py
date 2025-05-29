# data.py

def get_menus():
    return {
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
