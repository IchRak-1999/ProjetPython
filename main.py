from data_manipulation import readData
from dash import html
import dash
import pandas as pd
from dash import Dash, dcc

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

data = pd.read_excel("nombre_debit_departement.xlsx")


fileName = "nombre_debit_departement.xlsx"
data = readData(fileName)
# print(data)

app = dash.Dash(__name__)

app.title = "Débit"

# Interface de la dashboard
app.layout = html.Div([
    # Titre
    html.H1("DEBIT", style={'color': '#7E7288', 'textAlign': 'center'}),

    dcc.Graph(
        id="map",
    )

], style={'overflowX': 'hidden'})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Application ...')
    app.run_server(debug=True)

