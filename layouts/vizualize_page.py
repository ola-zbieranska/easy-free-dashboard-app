import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output
import dash
import plotly.express as px
def get_vizualize_page():
    vizualize_page = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div([
                html.P(
                    "If you need help learn how to create your first chart step by step click below to check out tutorials and documentation.")
            ]))
        ),
        dbc.Row([
            dbc.Col(html.Div([
                dcc.Tabs(id="tabs-visualize-menu", value='tab-1', children=[
                    dcc.Tab(label='Chart', value='tab-1'),
                    dcc.Tab(label='Refine', value='tab-2'),
                    dcc.Tab(label='Annotate', value='tab-3'),
                    dcc.Tab(label='Layout', value='tab-4')
                ])
            ]), width=4),
            dbc.Col(html.Div([
                dcc.Graph(id='graph-output')
            ]), width=8),
        ]),
        html.Div(id='tabs-content-visualize'),
        dbc.Button("Back", id="back-to-input", color="secondary", className="mt-2 me-2", href="/first-page"),
        dbc.Button("Next", id="proceed-to-visualize", color="primary", className="mt-2", href="")
    ])
    return vizualize_page