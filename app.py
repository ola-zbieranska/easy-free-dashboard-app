import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

import base64
import io
import datetime

#-------------------------------------------------------------------------
#Load chart templates for all available Bootstrap themes
load_figure_template('LUX')

# Initialize the app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

#-------------------------------------------------------------------------
#Components

#Style

# Definicja stylu dla paska bocznego (sidebar)

SIDEBAR_STYLE = {
    # Usunięto position: fixed, aby pozwolić na normalny przepływ dokumentu
    "top": "60px",
    "left": 0,  # Lewa granica
    "bottom": 0,  # Dolna granica
    "width": "24rem",  # Szerokość paska bocznego
    "padding": "2rem 1rem",  # Wewnętrzne odstępy
    "background-color": "#f8f9fa",  # Kolor tła
}

# Styl dla boxa na przesyłanie plików
UPLOAD_STYLE = {
    'width': '24rem',
    'height': '60px',
    'lineHeight': '60px',
    'borderWidth': '1px',
    'borderStyle': 'dashed',
    'borderRadius': '5px',
    'textAlign': 'center',
    'margin-bottom': '2rem',  # Dodaj odstęp od dolnego komponentu
}

#-------------------------------------------------------------------------
#Layout

#User interface for uploading files with specific style settings. Users can transfer single files

app.layout = html.Div([
dbc.Row([
        dbc.Col(),
        dbc.Col(html.H1('Welcome to my dash app: EASY DASHBOARD'), width=9, style={'margin-left': '7px', 'margin-top': '7px'})
    ]),
    dbc.Container([
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Przeciągnij i upuść lub ',
                html.A('wybierz plik')
            ]),
            style=UPLOAD_STYLE,
            multiple=False
        ),
        html.Div(
            [
                html.H2("Filters", style={"padding-top": "2rem"}),
                html.Hr(),
                html.P("A simple sidebar layout with filters", className="lead"),
                dbc.Nav(
                    [
                        dcc.Dropdown(id='dropdown-one', options=["test"]),  # Pusty dropdown, wypełnij opcjami
                        html.Br(),
                        dcc.Dropdown(id='dropdown-two', options=["test"]),  # Pusty dropdown, wypełnij opcjami
                        html.Br(),
                        dcc.Dropdown(id='dropdown-three', options=["test"])  # Pusty dropdown, wypełnij opcjami
                    ],
                    vertical=True,
                    pills=True,
                ),
            ],
            style=SIDEBAR_STYLE
        ),
        # Tutaj mogą zostać dodane inne komponenty, które będą wyświetlane obok sidebar
    ], fluid=True)
], style={"margin": "0px"})

#-------------------------------------------------------------------------
#Callback

# Callback for processing the uploaded file
@app.callback(
    Output('output-data-upload', 'children'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
    State('upload-data', 'last_modified')
)
def update_output(contents, filename, last_modified):
    if contents is not None:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        try:
            if 'csv' in filename:
                # Przyjmujemy, że użytkownik przesyła plik CSV
                df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
                return html.Div([
                    html.H5(filename),
                    html.H6(datetime.datetime.fromtimestamp(last_modified)),

                    dcc.Graph(
                        figure={
                            'data': [{'x': df[df.columns[0]], 'y': df[df.columns[1]], 'type': 'bar'}]
                        }
                    ),

                    html.Hr(),  # Linia pozioma

                    html.Div('Surowe zawartości pliku CSV:'),
                    html.Pre(contents[:200] + '...', style={
                        'whiteSpace': 'pre-wrap',
                        'wordBreak': 'break-all'
                    })
                ])
            else:
                return html.Div([
                    'Ten typ pliku nie jest obsługiwany.'
                ])
        except Exception as e:
            print(e)
            return html.Div([
                'Wystąpił błąd podczas przetwarzania pliku.'
            ])
    return html.Div([
        'Prześlij plik, aby zobaczyć jego zawartość.'
    ])



#-------------------------------------------------------------------------
# Run the app

if __name__ == '__main__':
    app.run_server(debug=True)
