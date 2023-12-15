import folium as folium

from data_manipulation import readData,getPourcentageDebitFigure,displayMap,histDebitNational
from dash import html
import dash
import pandas as pd
from dash import Dash, dcc

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

fileName = "Pourcentage_debit_departement.xlsx"
data = readData(fileName)
nomRegion = data["Région"]

app = dash.Dash(__name__)

app.title = "Débit"

# Créer une carte Folium
mymap = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

# Interface de la dashboard
app.layout = html.Div([
    # Titre
    html.H1("DEBIT", style={'color': '#7E7288', 'textAlign': 'center'}),

    # Ajouter le map
    html.Iframe(id='map', srcDoc=mymap._repr_html_(), width='100%', height='450'),

    dcc.Graph(
        id="map",
        figure = getPourcentageDebitFigure(data)
    ),
    dcc.Graph(
        figure=displayMap()
    ),
    dcc.Graph(
        figure=histDebitNational()
    ),

], style={'overflowX': 'hidden'})

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Application ...')
    app.run_server(debug=True)

