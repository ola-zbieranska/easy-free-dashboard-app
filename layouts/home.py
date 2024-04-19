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
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            },
            # Wielokrotne pliki
            multiple=True
        ),
        html.Div(id='output-data-upload')
    ])

# Definicja głównego układu dla strony głównej
def get_layout():
    layout = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div("Easy Dashboard"), width=12)
        ),
        upload_component(),
        dbc.Row([
            dbc.Col(html.Div([html.P("Treść Kwadratu 1", className="square-text"), html.Button("Przycisk 1", id='button-1', className="square-button")], className="square"), width=3),
            dbc.Col(html.Div([html.P("Treść Kwadratu 2",  className="square-text"), html.Button("Przycisk 2", id='button-2', className="square-button")], className="square"), width=3),
            dbc.Col(html.Div([html.P("Treść Kwadratu 3",  className="square-text"), html.Button("Przycisk 3", id='button-3', className="square-button")], className="square"), width=3),
            dbc.Col(html.Div([html.P("Treść Kwadratu 4",  className="square-text"), html.Button("Przycisk 4", id='button-4', className="square-button")], className="square"), width=3)
        ])
    ], fluid=True)
    return layout