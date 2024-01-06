#README.md

### Descritpion
Ce projet Python vise à simplifier la création de graphiques pour un tableau de bord en utilisant des données extraites de tableurs Excel. Les tableurs sélectionnés contiennent des informations sur la vitesse des débits Internet, classées par régions en France. L'outil automatise le processus de collecte, de traitement et de visualisation des données, offrant ainsi une solution efficace pour générer des rapports visuels instantanés sur la qualité des connexions Internet dans différentes régions du pays. Ce projet facilite la prise de décision et la compréhension rapide des variations de débits Internet à travers une interface dynamique.

###  Installation
Il faut cloner l'url du projet sur un terminal avec la commande:
```bash
$ git clone https://github.com/IchRak-1999/ProjetPython.git
```
(Il faut s'assurer d'être sur la branche master)

####  **REQUIREMENTS**
Un fichier Requirements.txt est joint contenant les packages à installer

### Déploiement
Pour lancer le dashboard (obrenir l'adresse du dash) utiliser la commande:
```bash
$ python main.py
```
Il est important de rentrer le bon path où le projet est cloné dans votre machine

### Analyse de données:

- Les donnés en question sont répartis sur les 13 régions de la France, montrant la couverture des différents débits selon les habitants de chaque région.
- On retrouve également un recensement national, qui donne une moyenne nationale, toujours selon les différents débits disponibles en France (0,5mbits,3mbits,8mbits,30mbits, 100mbits et 1gb).
- Globalement la couverture de ces débits est décroissante en allant du débit le plus bas au plus haut. Ce fait est partagé entre toutes les régions.
- Passant d'une couverture presque totale pour un débit de 0,5mbits/s à pas plus de 20% pour le plus débit le plus rapide.
- Les histogrammes montrent les régions avec la plus large couverture, on remarque par exemple pour le débit de à 30mbits/s que c'est la corse qui bénificie de la plus grande couverture avec plus de 20% sur la région.

# Guide du Développeur - Projet Débit Dashboard

Ce guide fournit des informations essentielles pour comprendre et contribuer au projet Débit Dashboard, un outil Python qui automatise la création de graphiques basés sur des données extraites de tableurs Excel, en se concentrant sur les débits Internet par région en France.

## 1. Structure du Projet

Le projet est composé des fichiers suivants :

- **data_manipulation.py**: Ce fichier contient des fonctions pour lire les données à partir d'un fichier Excel et générer des graphiques.

- **main.py**: Ce script utilise la bibliothèque Dash pour créer une interface utilisateur basée sur le web qui affiche les graphiques générés par les fonctions de `data_manipulation.py`. Il intègre également des fonctionnalités de mise à jour en temps réel à l'aide de Dash callbacks.

- **Pourcentage_debit_daptement.xlsx, Pourcentage_debit_national.xlsx, data.xlsx, departements-region.json, nombre_debit_departement.xlsx, pourcentage_debit_region.xlsx**: Des fichiers de données et de configuration nécessaires pour l'exécution du projet.

## 2. Fichier `data_manipulation.py`

### Fonctions Principales :

1. **`readData(fileName)`**: Cette fonction lit les données à partir d'un fichier Excel et renvoie le DataFrame correspondant.

2. **`histDebitNational()`**: Cette fonction génère un graphique de type entonnoir (funnel) montrant le pourcentage du débit national.

3. **`graph_hist()`**: Cette fonction génère un histogramme montrant le pourcentage du débit par département.

## 3. Fichier `main.py`

### Composants Dash Principaux :

1. **Interface Dash**: Le script crée une interface utilisateur Dash comprenant un titre, un sélecteur de vitesse de débit, des graphiques interactifs et des mises à jour en temps réel.

2. **Callbacks Dash**:
    - **`UpdatePourcentageDebitFigure(bit)`**: Met à jour le graphique de pourcentage de débit en fonction de la vitesse de débit sélectionnée.
    - **`display_choropleth_map_Update(bit)`**: Met à jour la carte choroplèthe en fonction de la vitesse de débit sélectionnée.

## 4. Utilisation du Projet

1. **Installation des Dépendances**:
   - Assurez-vous d'avoir les bibliothèques Plotly, Dash et pandas installées : `pip install plotly dash pandas`.


2. **Personnalisation**:
   - Modifiez les fichiers de données au besoin pour mettre à jour les informations affichées dans les graphiques.

## 5. Remarque

- Assurez-vous que les fichiers de données sont correctement nommés et situés dans le répertoire du projet.