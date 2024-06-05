import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from geopy.geocoders import Nominatim
import pycountry

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


