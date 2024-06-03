import dash
import pandas as pd
import pycountry
from geopy.geocoders import Nominatim
import plotly.express as px
import plotly.graph_objects as go
from dash import Input, Output, State, html
import base64
import io

def map_country_names_to_iso_alpha3(df, location_col):
    country_to_iso = {country.name: country.alpha_3 for country in pycountry.countries}
    df['ISO_alpha_3'] = df[location_col].map(country_to_iso)
    return df

def add_lat_lon(df, location_col, type_col):
    geolocator = Nominatim(user_agent="geoapiExercises")
    latitudes = []
    longitudes = []
    for index, row in df.iterrows():
        location = None
        if row[type_col] in ['Country', 'City', 'Region']:
            location = geolocator.geocode(row[location_col])
        elif row[type_col] == 'Point':
            coords = row[location_col].split(',')
            latitudes.append(float(coords[0]))
            longitudes.append(float(coords[1]))
            continue

        if location:
            latitudes.append(location.latitude)
            longitudes.append(location.longitude)
        else:
            latitudes.append(None)
            longitudes.append(None)

    df['Latitude'] = latitudes
    df['Longitude'] = longitudes
    return df

def generate_scatter_map(df, template):
    return px.scatter_geo(df, lat='Latitude', lon='Longitude', color="Location",
                          hover_name="Location", projection="natural earth", title='Scatter Map', template=template)

def generate_heatmap(df, template):
    fig = go.Figure(go.Densitymapbox(lat=df.Latitude, lon=df.Longitude, z=[1] * len(df), radius=10))
    fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=0, mapbox_center_lat=0,
                      mapbox_zoom=1, title='Heatmap', template=template)
    return fig

def generate_bubble_map(df, size_col, template):
    return px.scatter_geo(df, lat='Latitude', lon='Longitude', size=size_col,
                          color="Location", hover_name="Location",
                          projection="natural earth", title='Bubble Map', template=template)

def register_map_callbacks(app):
    @app.callback(
        Output('graph-output-map', 'figure'),
        [Input('scatter-map', 'n_clicks'),
         Input('heatmap', 'n_clicks'),
         Input('bubble-map', 'n_clicks')],
        [State('upload-data', 'contents'),
         State('upload-data', 'filename'),
         State('data-input', 'value'),
         State('template-dropdown', 'value')]
    )
    def update_map(scatter_clicks, heatmap_clicks, bubble_clicks, contents, filename, data_value, template):
        ctx = dash.callback_context
        if not ctx.triggered or contents is None:
            return {}

        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        try:
            if 'csv' in filename:
                df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
            elif 'xls' in filename:
                df = pd.read_excel(io.BytesIO(decoded))
            else:
                return html.Div(['Unsupported file format.'])

            if 'Location' in df.columns and 'Type' in df.columns:
                df = add_lat_lon(df, 'Location', 'Type')
            else:
                return html.Div(['The file must contain "Location" and "Type" columns.'])

            if button_id == 'scatter-map':
                return generate_scatter_map(df, template)
            elif button_id == 'heatmap':
                return generate_heatmap(df, template)
            elif button_id == 'bubble-map':
                size_col = df.columns[2]
                if size_col not in ['Latitude', 'Longitude']:
                    return generate_bubble_map(df, size_col, template)
                else:
                    return html.Div(['The file must contain a data column for Bubble Map.'])
        except Exception as e:
            return html.Div(['There was an error processing this file.'])

