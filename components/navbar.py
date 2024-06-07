import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

def get_navbar():
    """
       Tworzy i zwraca nawigację aplikacji.
       Creates and returns the navigation bar.

       Returns:
           dbc.NavbarSimple: Nawigacja.
                             Navigation bar.
       """
    # Menu przełączania motywu (jasny/ciemny)
    # Theme toggle menu (light/dark)
    theme_toggle = dbc.DropdownMenu(
        label=html.I(className="bi bi-brightness-high-fill"),
        children=[
            dbc.DropdownMenuItem([html.I(className="bi bi-brightness-high-fill me-2"), "Light"], id="light-mode", n_clicks=0,
                                 className="dropdown-item"),
            dbc.DropdownMenuItem([html.I(className="bi bi-moon-fill me-2"), "Dark"], id="dark-mode", n_clicks=0,
                                 className="dropdown-item"),
        ],
        className="theme-switch-container",
        id="theme-dropdown"
    )
    # Menu rozwijane z dodatkowymi stronami
    # Dropdown menu with additional pages
    dropdown = dbc.DropdownMenu(
        children=[
            dbc.DropdownMenuItem("More pages", header=True),
            dbc.DropdownMenuItem("Main", href="/home"),
            dbc.DropdownMenuItem("Create", href="/create-page"),
            dbc.DropdownMenuItem("Blog", href="/blog"),
            dbc.DropdownMenuItem("Documentation", href="/documentation"),
            dbc.DropdownMenuItem("Visualize data", href="/vizualize-page"),
            dbc.DropdownMenuItem("Check Data", href="/check-data-page"),
            dbc.DropdownMenuItem("Publish chart", href="/publish-page")
        ],
        nav=True,
        in_navbar=True,
        label="More",
    )
    # Przycisk do repozytorium GitHub
    # Button to the GitHub repository
    github_button = dbc.Button(
        html.I(className="bi bi-github"),
        color="link",
        href="https://github.com/ola-zbieranska/easy-free-dashboard-app",
        external_link=True,
        className="me-2",
        target="_blank"
    )
    # Definicja głównej nawigacji aplikacji
    # Definition of the main navigation bar of the application
    navbar = dbc.NavbarSimple(
        children=[
            github_button,
            theme_toggle,
            dbc.NavItem(dbc.NavLink("Main", href="/home")),
            dbc.NavItem(dbc.NavLink("Create", href="/create-page")),
            dropdown
        ],
        brand="Easy Dashboard",
        brand_href="/home",
        sticky="top",
        color="primary",
        dark=True,
    )
    return navbar