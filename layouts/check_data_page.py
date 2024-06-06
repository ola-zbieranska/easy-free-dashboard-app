import dash_bootstrap_components as dbc
from dash import html, dcc, dash_table

def get_check_data_page():
    check_data_page = dbc.Container([
        dbc.Row(
            dbc.Col(
                html.Div([
                    html.H1("Make sure the data looks right"),
                    html.P([
                        "Please make sure that Easy Dashboard interprets your data correctly.",
                        html.Br(),
                        "The text data should be in English.",
                        html.Br(),
                        "In the table:",
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
                ])
            )
        ),
        dbc.Row(
            dbc.Col(
                html.Div([
                    dbc.Checkbox(id='first-row-header', label="First row as label", className="mt-2"),
                    dash_table.DataTable(
                        id='data-table',
                        columns=[],
                        data=[],
                        editable=True,
                        row_deletable=True,
                        style_table={'height': '300px', 'overflowY': 'auto'},
                        style_cell={'textAlign': 'left'},
                    )
                ]), width=12
            )
        ),
        dbc.Row(
            dbc.Col(
                html.Div([
                    dbc.Button("Back", color="secondary", href="/create-page", className="mt-2 me-2"),
                    dbc.Button("Next", color="primary", href="/vizualize-page", className="mt-2")
                ])
            )
        ),
        dcc.Store(id='stored-data'),  # Dodaj tutaj komponent dcc.Store
    ])
    return check_data_page