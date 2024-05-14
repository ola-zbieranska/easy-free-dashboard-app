import dash_bootstrap_components as dbc
from dash import html, dcc

# Definicja trzech różnych kart
card1 = dbc.Card(
    [
        #dbc.CardHeader("Copy & paste data table"),
        dbc.CardBody(
            [
                html.H4("Copy & paste your data", className="card-title"),
                #html.P("Select your data in Excel or LibreOffice and paste it in the text field", className="card-text"),
            ]
        ),
        dbc.CardFooter(dbc.Button("Copy & Paste", color="primary",href="/copy-paste-data-page")),
    ],
    style={"width": "18rem"},
)

card2 = dbc.Card(
    [
        #dbc.CardHeader("CSV/Excel upload"),
        dbc.CardBody(
            [
                html.H4("Upload CSV or Excel spreadsheets", className="card-title"),
                #html.P("Upload a CSV or Excel file from your computer", className="card-text"),
            ]
        ),
        dbc.CardFooter(dbc.Button("Choose File", color="primary", href="/upload-data-page")),
    ],
    style={"width": "18rem"},
)

card3 = dbc.Card(
    [
        #dbc.CardHeader("Connect Google Sheet"),
        dbc.CardBody(
            [
                html.H4("Connect Google Sheet", className="card-title"),
                #html.P("Make sure to enable Link Sharing in the Google Sheet and copy the spreadsheet URL into the text field on the right", className="card-text"),
            ]
        ),
        dbc.CardFooter(dbc.Button("Connect Sheet", color="primary", href="/import-data-page")),
    ],
    style={"width": "18rem"},
)

# Funkcja generująca pierwszą stronę
def get_first_page():
    first_page = dbc.Container([
        dbc.Row(
            dbc.Col(html.Div([
                html.H1("Create custom charts and dashboard in an easy & free way."),
                html.P("If you need help learn how to create your first chart step by step click below to check out tutorials and documentation."),
                dbc.Button("Learn more", color="primary", href="/documentation", className="me-1"),
                html.H3("First Step: How do you want to upload your data?")
            ]))
        ),
        dbc.Row(
            dbc.Col(
                dbc.CardGroup(
                    [card1, card2, card3]
                ),
                width=12
            ),
            className="mt-4"  # margines górny
        ),
    ])
    return first_page
