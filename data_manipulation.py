import pandas as pd
import plotly.express as px

def readData(fileName):
    data = pd.read_excel(fileName)
    return data
    """
    print(data["Région"])
    """

def getPourcentageDebitFigure(data):
    map = px.line(data,x=data['Région'],y=data['Nombre de locaux'], title='Pourcentage de débit par région')
    return map

def displayMap():
     data = readData('Pourcentage_debit_national.xlsx')

     # Couleur carte : blanc -> jaune -> rouge
     #colorscale = ["rgb(255,255,255)", "rgb(255,226,58)", "rgb(245,164,12)", "rgb(255,150,150"]
"""
     map = px.choropleth_mapbox(data,
         center = {"lon": -2.573158317817201, "lat": 46.75212876753963},
         color_continuous_scale = colorscale,
         color_continuous_midpoint = 0
     )"""


def histDebitNational():
    data = readData('Pourcentage_debit_national.xlsx')
    mbit = ['0,5 Mbit/s','3 Mbit/s','8 Mbit/s','30 Mbit/s']
    debit = data[mbit]

    fig = px.histogram(debit)
    return  fig
