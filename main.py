import pandas as pd
from dash import dash_table, Output, Input
from data_manipulation import readData, histDebitNational, graph_hist
from dash import html
import dash
import plotly.express as px
from dash import Dash, dcc
import json

with open("departements-region.json") as response:
    GEOJSON = json.load(response)

fileName = "Pourcentage_debit_departement.xlsx"
data = readData(fileName)
regions = data['Région']

app = dash.Dash(__name__)
colors = {
    'background': '#000000',
    'text': '#7FDBFF'
}

app.title = "Débit"

histo = graph_hist()

histogramme_NBL_Region = html.Div(dcc.Graph(figure=histo, id='histo'),
                                  style={'display': 'inline-block', 'width': '49%'})


@app.callback(
    Output('map', 'figure'),
    Input('dropdown', 'value')
)
def UpdateMap(bit):
    dataA = data[bit]
    mapA = px.scatter(x=data['Région'], y=dataA)
    return mapA


def CreateMap():
    # Graphe des points
    map = px.scatter(data, x="Région", y="0,5 Mbit/s")
    return map


@app.callback(
    Output('mapPD', 'figure'),
    Input('dropdown', 'value')
)
def UpdatePourcentageDebitFigure(bit):
    dataB = data[bit]
    mapB = px.line(x=data['Région'], y=dataB)
    return mapB

def display_choropleth_map(bit):
    dataMapDebit = data['0,5 Mbit/s']
    # Affichage de la carte
    fig = px.choropleth_mapbox(
        dataMapDebit, geojson=GEOJSON, locations=regions, color=bit,
        color_continuous_scale="Viridis",
        range_color=(0, 100),
        mapbox_style="carto-positron",
        featureidkey="properties.code",
        zoom=5, center={"lon": -2.573158317817201, "lat": 46.75212876753963},
        opacity=0.5,
        labels={'Région': 'Débit'}
    )

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig

@app.callback(
    Output("mapDebit", "figure"),
    Input("dropdown", "value"))
def display_choropleth_map_Update(bit):
    dataMapDebit = data[bit]
    # Affichage de la carte
    fig = px.choropleth_mapbox(
        dataMapDebit, geojson=GEOJSON, locations=regions, color=bit,
        color_continuous_scale="Viridis",
        color_continuous_midpoint=0,
        range_color=(0, 100),
        mapbox_style="carto-positron",
        featureidkey="properties.code",
        zoom=5, center={"lon": -2.573158317817201, "lat": 46.75212876753963},
        opacity=0.5,
        labels={'Région': 'Débit'}
    )

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig


def getPourcentageDebitFigure():
    map = px.line(data, x=data['Région'], y=data['0,5 Mbit/s'])
    return map


# Penser à ajouter des varaibles pour chaque élement et l'appeler
# Interface de dashboard
app.layout = html.Div([
    # Titre
    html.H1("DEBIT", style={'color': '#7E7288', 'textAlign': 'center'}),

    # Ajouter un saut de ligne
    html.Br(),

    html.H3('Pourcentage de débit par région:', style={'color': '#7E7288', 'textAlign': 'left', 'margin-left': '2%'}),

    # Le choix de vitesse debit/s
    dcc.Dropdown(id='dropdown',
                 options=[
                     {'label': '0,5 Mbit/s', 'value': '0,5 Mbit/s'},
                     {'label': '3 Mbit/s', 'value': '3 Mbit/s'},
                     {'label': '8 Mbit/s', 'value': '8 Mbit/s'},
                     {'label': '30 Mbit/s', 'value': '30 Mbit/s'},
                 ],
                 value='0,5 Mbit/s',
                 style={'width': '250px', 'margin-left': '2%'}
                 ),
    html.Br(),

    # Ajouter le map
    html.Div(dcc.Graph(
        id="map",
    ), style={'display': 'inline-block', 'width': '49%'}),

    # Ajouter le figure ligne
    html.Div(dcc.Graph(
        id="mapPD",
    ), style={'display': 'inline-block', 'width': '49%'}),

    # Ajouter le figure ligne
    html.Div(dcc.Graph(
        id="mapDebit",
    ), style={'display': 'inline-block', 'width': '85%', 'margin-left': '5%'}),

    # Ajouter une ligne horizontale
    html.Hr(),
    html.H3('Nombre de locaux par région:', style={'color': '#7E7288', 'textAlign': 'left'}),

    # Histogramme coloré
    html.Div(className='row', children=[
        dcc.Graph(
            figure=histDebitNational(),
        )], style={'display': 'inline-block', 'width': '49%'}),

    # Histogramme
    histogramme_NBL_Region,

], style={'overflowX': 'hidden'})

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Application ...')
    app.run_server(debug=True)
