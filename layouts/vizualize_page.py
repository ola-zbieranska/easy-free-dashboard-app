import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table


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
        dbc.Button([html.I(className="bi bi-graph-up me-2"), "Line Chart"], id="line-chart",
                   className="chart-button m-2"),
        dbc.Button([html.I(className="bi bi-dot me-2"), "Scatter Plot"], id="scatter-plot",
                   className="chart-button m-2"),
        dbc.Button([html.I(className="bi bi-bar-chart-fill me-2"), "Area Chart"], id="area-chart",
                   className="chart-button m-2"),
        dbc.Button([html.I(className="bi bi-bar-chart-fill me-2"), "Column Chart"], id="column-chart",
                   className="chart-button m-2"),
        dbc.Button([html.I(className="bi bi-table me-2"), "Table"], id="table", className="chart-button m-2"),
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
                dcc.Graph(id='graph-output'),
                dash_table.DataTable(id='table-output', style_table={'display': 'none'})
            ]), width=8),
        ]),
        html.Div(id='tabs-content-visualize'),
        dbc.Button("Back", color="secondary", href="/check-and-describe-page", className="mt-2 me-2"),
        dbc.Button("Next", color="primary", href="/publish-page", className="mt-2")
    ])

    return vizualize_page