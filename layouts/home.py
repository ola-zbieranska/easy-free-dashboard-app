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
        # Dodanie komponentu uploadu plików do głównej strony
        upload_component()
    ], fluid=True)
    return layout
