import dash_bootstrap_components as dbc
from dash import html, dcc
def get_publish_page():
    publish_page = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div([
                html.H1("Publish visualization"),
                html.H1("Embed your chart or download it as PNG."),
                dbc.Button("Publish", color="primary", href="/", className="me-1")
            ]))
        )
    ])
    return publish_page