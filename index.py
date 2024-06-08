import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from app import app
from components.navbar import get_navbar as navbar
from callbacks.app_callbacks import register_app_callbacks
from callbacks.data_callbacks import register_data_callbacks
from callbacks.visualization_callbacks import register_visualization_callbacks

server = app.server

# Setting the main application layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar(),
    dcc.Store(id='theme-store', data={'theme': dbc.themes.FLATLY}),
    dcc.Store(id='stored-data'),
    html.Link(id='theme-link', rel='stylesheet', href=dbc.themes.FLATLY),
    html.Div(id='page-content', className='light-mode')
])

# Registration of all callbacks
register_app_callbacks(app)
register_data_callbacks(app)
register_visualization_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)