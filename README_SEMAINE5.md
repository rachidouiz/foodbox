# Semaine 5 – Intégration d’une base de données (SQL)

---

## Réalisations

-  **Modèles créés avec SQLAlchemy** :
  - "Plat" : représente chaque plat avec son nom, prix et catégorie.
  - "Commande" : enregistre les informations du client et la date de commande.
  - "ArticleCommande" : stocke chaque ligne de commande (plat + quantité).

-  **Création automatique du schéma avec "db.create_all()"**

- **Ajout d’un script "populate_db.py"** :
  - Remplit automatiquement la base avec les plats de déjeuner et dîner/souper.

- **Refonte de la logique de menu** :
  - Les données ne viennent plus du fichier "data.py", mais de la base SQLite.
  - La fonction "get_menu_by_name(nom_menu)" dans "services.py" regroupe les plats par catégorie depuis la base.

## Gestion du panier inchangée 
(stocké en session côté Flask).

---

## Fichiers clés

- "models.py" : contient les définitions de la base
- "populate_db.py" : initialise et remplit la base
- "services.py" : charge dynamiquement le menu depuis la base
- "app.py" : contient l’application Flask avec les routes mises à jour

---

## Résultat

-L’application est maintenant entièrement connectée à une base SQLite.  
-Les menus sont dynamiques et modifiables facilement via la base.  
-Le panier et la commande fonctionnent comme avant.