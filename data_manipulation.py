import pandas as pd
import plotly.express as px


def readData(fileName):
    """
        Lire les donées depuis un fichier Excel

           Args:
               - fileNme: contient le nom de fichier

           Returns:
               Les données de le fichier fileName
    """
    # Lire les données de fichier Excel
    data = pd.read_excel(fileName)
    return data


def histDebitNational():
    """
       Affichage de la graphe funnel de débit national

           Returns:
               Affiche la graphe funnel (fig)
           """
    # Afficher le pourcentage de débit national
    data = dict(
        vitesse=['','0,5 Mbit/s', '3 Mbit/s', '8 Mbit/s', '30 Mbit/s'],
        pourcentage=['', '97,4%', '84,9%', '64,1%', '16,3%'])
    fig = px.funnel(data, x='vitesse', y='pourcentage', title='Pourcentage débit National')

    return fig


def graph_hist():
    """
        Affichage de la graphe de nombre des locaux national

           Returns:
               Affiche l'histogramme (fig)
           """
    # Afficher le nombre des locaux national
    data = readData("Pourcentage_debit_departement.xlsx")
    fig = px.histogram(data, x='Région', y='Nombre de locaux', title='Nombre des locaux par département')
    return fig
