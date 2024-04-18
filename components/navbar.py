import dash_bootstrap_components as dbc

def get_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Strona główna", href="/home")),
            dbc.NavItem(dbc.NavLink("O Aplikacji", href="/about")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("Profil", href="/profile"),
                    dbc.DropdownMenuItem("Ustawienia", href="/settings"),
                    dbc.DropdownMenuItem("Wyloguj", href="/logout"),
                ],
                nav=True,
                in_navbar=True,
                label="Twoje Konto",
            ),
        ],
        brand="easy dashboard",
        brand_href="/home",
        sticky="top",
        color="primary",
        dark=True,
        className="mb-4",  # Dodanie klasy stylu Bootstrap 'mb-4' (margin-bottom: 4)
    )
    return navbar