import pandas as pd
import plotly.express as px

def readData(fileName):
    data = pd.read_excel(fileName)
    return data

def histDebitNational():
    data = readData('Pourcentage_debit_departement.xlsx')
    mbit = ['0,5 Mbit/s','3 Mbit/s','8 Mbit/s','30 Mbit/s']
    debit = data[mbit]

    fig = px.histogram(debit)

    return fig

def graph_hist():
    fig = px.histogram(readData("Pourcentage_debit_departement.xlsx"), x='Région', y='Nombre de locaux')
    return fig

