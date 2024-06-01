import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table
def get_check_and_describe_page():
    check_and_describe_page = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div([
                html.H1("Make sure the data looks right"),
                html.P(["Please make sure that Easy Dashboard interprets your data correctly. The text data should be in English. In the table: ",
                    html.Br(),
                    html.Span("number", style={'color': 'blue'}),
                    " columns should be shown in blue,",
                    html.Br(),
                    html.Span("dates", style={'color': 'green'}),
                    " in green,",
                    html.Br(),
                    html.Span("text", style={'color': 'black'}),
                    " in black,",
                    html.Br(),
                    html.Span("red", style={'color': 'red'}),
                    " cell indicates a problem in your dataset that needs to be fixed,",
                    html.Br(),
                    html.Span("—", style={'color': 'gray'}),
                    " cells contain no data."
                ]),
                dbc.Row(dbc.Col(html.Div([
                    dbc.Checkbox(id='first-row-header', label="First row as label", className="mt-2"),
                    html.Label("Output locale"),
                    dcc.Dropdown(
                        id='output-locale',
                        options=[
                            {'label': 'English (en-US)', 'value': 'en-US'},
                            {'label': 'Polish (pl-PL)', 'value': 'pl-PL'}
                        ],
                        value='en-US',
                        className="mb-2"
                    ),
                    dash_table.DataTable(
                        id='data-table',
                        columns=[],
                        data=[],
                        editable=True,
                        row_deletable=True,
                        style_table={'height': '300px', 'overflowY': 'auto'},
                        style_cell={'textAlign': 'left'},
                    )
                ])),width=4),
                dbc.Row(dbc.Col(html.Div([
                    dash_table.DataTable(id='table-check-data', style_table={'display': 'none'})
                ]))),
                dbc.Button("Back", color="secondary", href="/first-page", className="mt-2 me-2"),
                dbc.Button("Next", color="primary", href="/vizualize-page", className="mt-2")
            ]))
        )
    ])
    return check_and_describe_page