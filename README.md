# TP-Python-IA
Classificateur Arbre de Décision pour les Données Clients
Ce projet implémente un classificateur Arbre de Décision pour analyser un jeu de données de clients. Le modèle utilise l'âge, le revenu, le statut d'étudiant et le statut de crédit pour prédire si un client effectuera un achat ou non.

Structure du Projet
dataset_clients.csv : Le jeu de données client avec des champs tels que Age, Revenu, Étudiant, Crédit, et Acheter.
TP1.py : Script Python qui encode les données catégorielles, entraîne un modèle d’arbre de décision, et visualise l'arbre de décision.
Caractéristiques
Les caractéristiques suivantes sont utilisées pour entraîner le classificateur d’arbre de décision :

Age : L'âge du client.
Revenu : Le niveau de revenu du client (Faible, Moyen, Haut).
Étudiant : Indique si le client est étudiant (Oui ou Non).
Crédit : Statut de crédit du client (Oui ou Non).
La variable cible est :

Acheter : Indique si le client a effectué un achat (Oui ou Non).
Prise en Main
Prérequis
Assurez-vous d'avoir Python installé avec les bibliothèques suivantes :

pandas
scikit-learn
matplotlib
Vous pouvez installer les packages requis avec :


pip install pandas scikit-learn matplotlib
Utilisation
Clonez le dépôt sur votre machine locale.
Placez votre jeu de données client sous le nom dataset_clients.csv ou modifiez le script pour utiliser vos propres données.
Exécutez le script :

python TP1.py

Vue d’Ensemble du Code
Le script effectue les étapes suivantes :

Encodage des Données : Les caractéristiques catégorielles sont encodées en valeurs numériques pour être compatibles avec le classificateur d'arbre de décision de scikit-learn.
Entraînement du Modèle : Un modèle de Classificateur Arbre de Décision est entraîné sur les caractéristiques.
Évaluation du Modèle : La précision du modèle est calculée et affichée.
Visualisation de l'Arbre de Décision : L’arbre de décision est visualisé, montrant les séparations et l’importance des caractéristiques.
Résultats
L’arbre de décision fournit des indications sur la façon dont les caractéristiques telles que l'âge, le revenu, le statut d'étudiant et le statut de crédit influencent la décision d'achat des clients. La précision du modèle est affichée lors de l'exécution, ainsi qu'une visualisation de l'arbre de décision.

