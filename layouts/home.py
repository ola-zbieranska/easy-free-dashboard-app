import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div("Easy Dashboard"), width=12)
    ]),
    dbc.Row([
        dbc.Col(html.Div())
    ])