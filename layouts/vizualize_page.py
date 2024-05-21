import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output
import dash
import plotly.express as px
def get_vizualize_page():
    chart_buttons = [
        dbc.Button([html.I(className="bi bi-bar-chart-fill me-2"), "Bar Chart"], id="bar-chart",
                   className="chart-button m-2"),
        dbc.Button([html.I(className="bi bi-bar-chart-steps me-2"), "Stacked Bars"], id="stacked-bars",
                   className="chart-button m-2"),
        dbc.Button([html.I(className="bi bi-bar-chart me-2"), "Grouped Bars"], id="grouped-bars",
                   className="chart-button m-2"),
        dbc.Button([html.I(className="bi bi-pie-chart-fill me-2"), "Pie Chart"], id="pie-chart",
                   className="chart-button m-2"),
        # dodać później więcej przycisków dla innych typów wykresów
    ]
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
                    dcc.Tab(label='Chart', value='tab-1', children=chart_buttons),
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
        dbc.Button("Back", id="viz-back-to-input", color="secondary", className="mt-2 me-2"),
        dbc.Button("Next", id="viz-proceed-to-visualize", color="primary", className="mt-2")
    ])
    return vizualize_page