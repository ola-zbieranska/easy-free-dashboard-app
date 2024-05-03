import dash_bootstrap_components as dbc
from components.navbar import get_navbar
from components.sidebar import get_sidebar
from layouts.home import get_layout as home_layout
from callbacks.callbacks import *

# Ustawienie głównego układu aplikacji
app.layout = dbc.Container([
    get_navbar(),
    get_sidebar(),
    home_layout(),


], fluid=True)

# Uruchomienie
if __name__ == '__main__':
    app.run_server(debug=True)