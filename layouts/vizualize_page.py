import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table


def get_vizualize_page():
    chart_buttons = [
        dbc.Button([html.I(className="bi bi-bar-chart-fill me-2"), "Bar Chart"], id="bar-chart",
                   className="chart-button m-2"),
        dbc.Button([html.I(className="bi bi-pie-chart-fill me-2"), "Pie Chart"], id="pie-chart",
                   className="chart-button m-2"),
        dbc.Button([html.I(className="bi bi-graph-up me-2"), "Line Chart"], id="line-chart",
                   className="chart-button m-2"),
        dbc.Button([html.I(className="bi bi-dot me-2"), "Scatter Plot"], id="scatter-plot",
                   className="chart-button m-2"),
        dbc.Button([html.I(className="bi bi-bar-chart-fill me-2"), "Area Chart"], id="area-chart",
                   className="chart-button m-2"),
        dbc.Button([html.I(className="bi bi-table me-2"), "Table"], id="table", className="chart-button m-2"),
        dbc.Button([html.I(className="bi bi-globe2 me-2"), "Scatter Map"], id="scatter-map",
                   className="chart-button m-2"),
        dbc.Button([html.I(className="bi bi-globe2 me-2"), "Heatmap"], id="heatmap",
                   className="chart-button m-2"),
        dbc.Button([html.I(className="bi bi-globe2 me-2"), "Bubble Map"], id="bubble-map",
                   className="chart-button m-2"),
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
                    dcc.Tab(label='Chart type', value='tab-1', children=chart_buttons),
                    dcc.Tab(label='Annotate', value='tab-2', children=[
                        html.Div([
                            html.Label("Chart Title: "),
                            dcc.Input(id="chart-title", type="text", value=""),
                            html.Br(),
                            html.Label("Show Legend"),
                            dcc.Checklist(id="show-legend", options=[{"label": "", "value": "show"}], value=["show"]),
                            html.Br()
                        ])
                    ]),
                    dcc.Tab(label='Refine', value='tab-3', children=[
                        html.Div([
                            html.P("available soon - work in progress")
                        ])
                    ]),
                    dcc.Tab(label='Layout', value='tab-4', children=[
                        html.Div([
                            html.P("available soon - work in progress")
                        ])
                    ])
                ])
            ]), width=4),
            dbc.Col(html.Div([
                dcc.Graph(id='graph-output'),
                dash_table.DataTable(id='table-output', style_table={'display': 'none'}),
                dcc.Textarea(id='data-input', style={'display': 'none'}),  # Dodajemy ukryty element `data-input`
                dcc.Upload(id='upload-data', style={'display': 'none'}),  # Dodajemy ukryty element `upload-data`
                dcc.Input(id='google-sheet-url', type='url', style={'display': 'none'})  # Dodajemy ukryty element `google-sheet-url`
            ]), width=8),
        ]),
        html.Div(id='tabs-content-visualize'),
        dbc.Button("Back", color="secondary", href="/check-and-describe-page", className="mt-2 me-2"),
        dbc.Button("Next", color="primary", href="/publish-page", className="mt-2")
    ])

    return vizualize_page