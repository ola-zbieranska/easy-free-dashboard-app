import dash_bootstrap_components as dbc
from dash import html, dcc

# Funkcja importująca komponent uploadu plików
def upload_component():
    return html.Div([
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select Files')
            ]),
            className='upload-data-container',
            multiple=True
        ),
        html.Div(id='output-data-upload')
    ])

# Definicja głównego układu dla strony głównej
def get_layout():
    layout = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div(), width=12)
        ),
        dbc.Row([
            dbc.Col(html.Div([
                html.P("Upload CSV or Excel spreadsheets"),
                upload_component(),
                html.Button("Przycisk 1", id='button-1', className="square-button")
            ], className="square"), width=3),
            dbc.Col(html.Div([
                html.P("Treść Kwadratu 2"),
                html.Button("Przycisk 2", id='button-2', className="square-button")
            ], className="square"), width=3),
            dbc.Col(html.Div([
                html.P("Treść Kwadratu 3"),
                html.Button("Przycisk 3", id='button-3', className="square-button")
            ], className="square"), width=3),
            dbc.Col(html.Div([
                html.P("Treść Kwadratu 4"),
                html.Button("Przycisk 4", id='button-4', className="square-button")
            ], className="square"), width=3),
        ])
    ], fluid=False, style={"marginLeft": "16rem"})
    return layout
