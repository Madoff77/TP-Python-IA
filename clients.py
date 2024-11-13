import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Chargement du dataset
df_expanded = pd.read_csv('dataset_clients.csv')

# Encodage des fonctionnalités catégorielles
df_encoded = df_expanded.copy()
df_encoded['Revenu'] = df_encoded['Revenu'].astype('category').cat.codes
df_encoded['Étudiant'] = df_encoded['Étudiant'].astype('category').cat.codes
df_encoded['Crédit'] = df_encoded['Crédit'].astype('category').cat.codes
df_encoded['Acheter'] = df_encoded['Acheter'].astype('category').cat.codes

# Définition des variables explicatives (X) et de la variable cible (y)
X = df_encoded[['Age', 'Revenu', 'Étudiant', 'Crédit']]
y = df_encoded['Acheter']

# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialisation et entraînement du classifieur d'arbre de décision
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Prédiction sur l'ensemble de test et calcul de la précision
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Affichage de l'arbre de décision
plt.figure(figsize=(20, 10))
plot_tree(clf, feature_names=['Age', 'Revenu', 'Étudiant', 'Crédit'],
          class_names=['Non', 'Oui'], filled=True)
plt.title(f"Decision Tree Classifier\nAccuracy: {accuracy:.2f}")
plt.show()
