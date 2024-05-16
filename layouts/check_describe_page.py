import dash_bootstrap_components as dbc
from dash import html, dcc
from dash import dash_table
def get_check_and_describe_page():
    check_and_describe_page = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div([
                html.H1("Make sure the data looks right"),
                html.P([
                    "Please make sure that Easy Dashboard interprets your data correctly. In the table ",
                    html.Span("number", style={'color': 'blue'}),
                    " columns should be shown in blue, ",
                    html.Span("dates", style={'color': 'green'}),
                    " in green and ",
                    html.Span("text", style={'color': 'black'}),
                    " in black. A ",
                    html.Span("red", style={'color': 'red'}),
                    " cell indicates a problem in your dataset that needs to be fixed. ",
                    html.Span("—", style={'color': 'gray'}),
                    " cells contain no data."
                ]),
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
                ),
                dbc.Button("Back", id="back-to-input", color="secondary", className="mt-2 me-2", href="/first-page"),
                dbc.Button("Next", id="proceed-to-visualize", color="primary", className="mt-2", href="/vizualize-page")
            ]))
        )
    ])
    return check_and_describe_page