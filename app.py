# Import packages

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input

# Initialize the app

app = dash.Dash(__name__)

#-------------------------------------------------------------------------
# Import and clean data (importing csv into pandas)

#df = pd.read_csv("")


#-------------------------------------------------------------------------
# App layout

app.layout = html.Div([
    html.Div(children='Hello World')
])

# Run the app

if __name__ == '__main__':
    app.run(debug=True)
