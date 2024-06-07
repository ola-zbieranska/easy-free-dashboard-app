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
                dcc.Tabs(id="tabs-visualize-menu", value='tab-1', className='custom-tab', children=[
                    dcc.Tab(label='Chart', value='tab-1', children=chart_buttons, className='tab'),
                    dcc.Tab(label='Layout', value='tab-4', children=[
                        html.Div([
                            html.Label("Select Plotly Template:"),
                            dcc.Dropdown(
                                id='template-dropdown',
                                options=[
                                    {'label': 'Plotly White', 'value': 'plotly_white'},
                                    {'label': 'Plotly Dark', 'value': 'plotly_dark'},
                                    {'label': 'Seaborn', 'value': 'seaborn'},
                                    {'label': 'Simple White', 'value': 'simple_white'},
                                    {'label': 'GGPlot2', 'value': 'ggplot2'}
                                ],
                                value='plotly_dark',
                                clearable=False
                            )
                        ])
                    ], className='tab'),
                    dcc.Tab(label='Description', value='tab-2', children=[
                        html.Div([
                            html.P("available soon - work in progress")
                        ])
                    ], className='tab'),
                    dcc.Tab(label='Customize', value='tab-3', children=[
                        html.Div([
                            html.P("available soon - work in progress")
                        ])
                    ], className='tab'),
                ])
            ]), width=4),
            dbc.Col(html.Div([
                dcc.Graph(id='graph-output'),
                dash_table.DataTable(id='table-output', style_table={'display': 'none'}),
                dcc.Textarea(id='data-input', style={'display': 'none'}),
                dcc.Upload(id='upload-data', style={'display': 'none'}),
                dcc.Input(id='google-sheet-url', type='url', style={'display': 'none'})
            ]), width=8),
        ]),
        dcc.Store(id='stored-data'),
        html.Div(id='tabs-content-visualize'),
        dbc.Button("Back", color="secondary", href="/create-page", className="mt-2 me-2"),
        dbc.Button("Next", color="primary", href="/check-data-page", className="mt-2")
    ])

    return vizualize_page