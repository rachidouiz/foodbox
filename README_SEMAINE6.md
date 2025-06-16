# Semaine 6 — Tests de fonctionnement et documentation de l’architecture monolithique

# Tests de fonctionnement

Avant de finaliser l'intégration de la base de données, des tests manuels ont été réalisés pour valider les fonctionnalités suivantes :

- L'application se lance correctement ("app.py") et la base de données SQLite est générée automatiquement.
- Le fichier "populate_db.py" permet d’ajouter les plats à la base (obligatoire pour voir les menus).
- Les menus s’affichent dynamiquement depuis la base ("/menu/dejeuner" et "/menu/diner_souper").
- L’ajout au panier fonctionne depuis les pages menu.
- Le panier affiche bien les articles ajoutés, avec calcul du total et gestion des quantités.
- Le formulaire de commande s’affiche et réinitialise le panier après soumission.
- Les routes "/ajouter/<index>" et "/retirer/<index>" fonctionnent.
- Le CSS s’applique bien via le fichier statique "style.css".

# Documentation de l’architecture monolithique

Cette application est développée avec une **architecture monolithique**.

### Définition

Dans une architecture monolithique, toutes les composantes de l'application sont réunies dans un seul projet :

- Le **front-end** (fichiers HTML et CSS),
- Le **back-end** (logique métier dans "app.py"),
- La **gestion des données** (modèles SQLAlchemy et base SQLite),
- Le **routing** (gestion des pages web avec Flask).

### Avantages

- Simplicité de mise en place.
- Facilité de test et de maintenance dans un seul codebase.
- Idéal pour les projets de petite à moyenne taille.

### Limites

- Moins adapté à une montée en charge importante.
- Difficile à séparer ou à répartir sur plusieurs serveurs.
- Peu flexible si on souhaite ajouter un front-end externe ou une API REST.

