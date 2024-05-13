import dash_bootstrap_components as dbc
from dash import html, dcc

# Definicja trzech różnych kart
card1 = dbc.Card(
    [
        dbc.CardHeader("Copy & paste data table"),
        dbc.CardBody(
            [
                html.H4("Copy & paste your data", className="card-title"),
                html.P("Select your data (including header row/column) in Excel or LibreOffice and paste it in the text field. ", className="card-text"),
            ]
        ),
        dbc.CardFooter("Footer 1"),
    ],
    style={"width": "18rem"},
)

card2 = dbc.Card(
    [
        dbc.CardHeader("CSV/Excel upload"),
        dbc.CardBody(
            [
                html.H4("Upload CSV or Excel spreadsheets", className="card-title"),
                html.P("Upload a CSV or Excel file from your computer.", className="card-text"),
            ]
        ),
        dbc.CardFooter("Footer 2"),
    ],
    style={"width": "18rem"},
)

card3 = dbc.Card(
    [
        dbc.CardHeader("Connect Google Sheet"),
        dbc.CardBody(
            [
                html.H4("Import data from Google Sheet", className="card-title"),
                html.P("Make sure to enable Link Sharing in the Google Sheet and copy the spreadsheet url into the text field on the right.", className="card-text"),
            ]
        ),
        dbc.CardFooter("Footer 3"),
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
            [
                dbc.Col(card1, width=4),
                dbc.Col(card2, width=4),
                dbc.Col(card3, width=4),
            ],
            className="mt-4"  # Margines górny dla estetyki
        ),
    ])
    return first_page
