import dash_bootstrap_components as dbc
from app import app
from components.navbar import get_navbar
from components.sidebar import get_sidebar
from layouts.home import get_layout as home_layout

# Ustawienie głównego układu aplikacji
app.layout = dbc.Container([
    get_navbar(),
    get_sidebar(),
    home_layout(),
    # Tutaj możesz dodać więcej layoutów z innych modułów
], fluid=True)

# Uruchomienie serwera Deweloperskiego
if __name__ == '__main__':
    app.run_server(debug=True)