from dash import html

import dash
import pandas as pd
from dash import Dash, dcc

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

data = pd.read_excel("data.xlsx")
for row in data:
    print(row)

app = dash.Dash(__name__)

# Interface de la dashboard
app.layout = html.Div([
    # Titre
    html.H1("DEBIT", style={'color': '#7E7288', 'textAlign': 'center'}),

], style={'overflowX': 'hidden'})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Application ...')
    app.run_server(debug=True)

