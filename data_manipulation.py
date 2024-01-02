import pandas as pd
import plotly.express as px


def readData(fileName):
    # Lire les données de fichier Excel
    data = pd.read_excel(fileName)
    return data


def histDebitNational():
    # Afficher le pourcentage de débit national
    data = dict(
        vitesse=['','0,5 Mbit/s', '3 Mbit/s', '8 Mbit/s', '30 Mbit/s'],
        pourcentage=['', '97,4%', '84,9%', '64,1%', '16,3%'])
    fig = px.funnel(data, x='vitesse', y='pourcentage', title='Pourcentage débit National')

    return fig


def graph_hist():
    # Afficher le pourcentage de débit par département
    data = readData("Pourcentage_debit_departement.xlsx")
    fig = px.histogram(data, x='Région', y='Nombre de locaux', title='Pourcentage Débit par département')
    return fig
