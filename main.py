from dash import Output, Input
from data_manipulation import readData, histDebitNational, graph_hist
from dash import html
import dash
import plotly.express as px
from dash import dcc

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
    """
        Mettre à jour l'affichage de la carte en fonction de vitesse de débit choisi

        Args:
            - bit: valeur contient la vitesse de débit

        Returns:
            Affiche la carte (mapA)
        """
    dataA = data[bit]
    mapA = px.scatter(x=data['Région'], y=dataA)
    return mapA


def CreateMap():
    """
        Affichage de la garphe avec la valeur par défaut (0,5 Mbit/s)

        Returns:
            Affiche la carte (map)
        """
    # Graphe des points
    map = px.scatter(data, x="Région", y="0,5 Mbit/s")
    return map


@app.callback(
    Output('mapPD', 'figure'),
    Input('dropdown', 'value')
)
def UpdatePourcentageDebitFigure(bit):
    """
        Mettre à jour l'affichage de la graphe en fonction de vitesse de débit choisi

        rgs:
            - bit: valeur contient la vitesse de débit

        Returns:
            Affiche la graphe (mapB)
        """
    dataB = data[bit]
    mapB = px.line(x=data['Région'], y=dataB)
    return mapB

def getPourcentageDebitFigure():
    """
         Affichage de la graphe line avec la valeur par défaut (0,5 Mbit/s)

            Returns:
                Affiche la garphe line (map)
            """
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

    # Ajouter une ligne horizontale
    html.Hr(),

    # Histogramme coloré
    html.Div(className='row', children=[
        dcc.Graph(
            figure=histDebitNational(),
        )], style={'display': 'inline-block', 'width': '49%'}),

    # Histogramme de nombre de locaux par région
    histogramme_NBL_Region,

], style={'overflowX': 'hidden'})

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Application ...')
    app.run_server(debug=True)
