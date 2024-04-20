import dash_bootstrap_components as dbc

def get_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Strona główna", href="/home", className="nav-link"), className="nav-item"),
            dbc.NavItem(dbc.NavLink("O Aplikacji", href="/about", className="nav-link"), className="nav-item"),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Profil", href="/profile", className="dropdown-item"),
                    dbc.DropdownMenuItem("Ustawienia", href="/settings", className="dropdown-item"),
                    dbc.DropdownMenuItem("Wyloguj", href="/logout", className="dropdown-item"),
                ],
                nav=True,
                in_navbar=True,
                label="Twoje Konto",
                className="dropdown-menu"
            ),
        ],
        brand="easy dashboard",
        brand_href="/home",
        sticky="top",
        color="primary",
        dark=True,
        className="mb-4 navbar",
        fluid=True
    )
    return navbar