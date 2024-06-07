import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from geopy.geocoders import Nominatim
import pycountry

def map_country_names_to_iso_alpha3(df, location_col):
    """
        Mapuje nazwy krajów do ich kodów ISO Alpha-3 w DataFrame.

        Args:
            df (pd.DataFrame): DataFrame zawierający kolumnę z nazwami krajów.
            location_col (str): Nazwa kolumny zawierającej nazwy krajów.

        Returns:
            pd.DataFrame: DataFrame z dodatkową kolumną ISO_alpha_3.

        Maps country names to their ISO Alpha-3 codes in the DataFrame.

        Args:
            df (pd.DataFrame): DataFrame containing the column with country names.
            location_col (str): Name of the column containing country names.

        Returns:
            pd.DataFrame: DataFrame with an additional ISO_alpha_3 column.
        """
    country_to_iso = {country.name: country.alpha_3 for country in pycountry.countries}
    df['ISO_alpha_3'] = df[location_col].map(country_to_iso)
    return df

def add_lat_lon(df, location_col, type_col):
    """
       Dodaje kolumny szerokości i długości geograficznej do DataFrame na podstawie lokalizacji.

       Args:
           df (pd.DataFrame): DataFrame zawierający kolumny z lokalizacjami.
           location_col (str): Nazwa kolumny zawierającej lokalizacje.
           type_col (str): Nazwa kolumny określającej typ lokalizacji (kraj, miasto, region, punkt).

       Returns:
           pd.DataFrame: DataFrame z dodatkowymi kolumnami Latitude i Longitude.

       Adds latitude and longitude columns to the DataFrame based on locations.

       Args:
           df (pd.DataFrame): DataFrame containing columns with locations.
           location_col (str): Name of the column containing locations.
           type_col (str): Name of the column specifying the type of location (country, city, region, point).

       Returns:
           pd.DataFrame: DataFrame with additional Latitude and Longitude columns.
       """
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
    """
        Generuje wykres punktowy mapy świata na podstawie danych lokalizacji.

        Args:
            df (pd.DataFrame): DataFrame zawierający kolumny Latitude, Longitude i Location.
            template (str): Nazwa szablonu Plotly do zastosowania.

        Returns:
            plotly.graph_objects.Figure: Wykres punktowy mapy świata.

        Generates a world map scatter plot based on location data.

        Args:
            df (pd.DataFrame): DataFrame containing Latitude, Longitude, and Location columns.
            template (str): Name of the Plotly template to apply.

        Returns:
            plotly.graph_objects.Figure: World map scatter plot.
        """
    return px.scatter_geo(df, lat='Latitude', lon='Longitude', color="Location",
                          hover_name="Location", projection="natural earth", title='Scatter Map', template=template)

def generate_heatmap(df, template):
    """
        Generuje mapę cieplną na podstawie danych lokalizacji.

        Args:
            df (pd.DataFrame): DataFrame zawierający kolumny Latitude i Longitude.
            template (str): Nazwa szablonu Plotly do zastosowania.

        Returns:
            plotly.graph_objects.Figure: Mapa cieplna.

        Generates a heatmap based on location data.

        Args:
            df (pd.DataFrame): DataFrame containing Latitude and Longitude columns.
            template (str): Name of the Plotly template to apply.

        Returns:
            plotly.graph_objects.Figure: Heatmap.
        """
    fig = go.Figure(go.Densitymapbox(lat=df.Latitude, lon=df.Longitude, z=[1] * len(df), radius=10))
    fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=0, mapbox_center_lat=0,
                      mapbox_zoom=1, title='Heatmap', template=template)
    return fig

def generate_bubble_map(df, size_col, template):
    """
        Generuje mapę bąbelkową na podstawie danych lokalizacji i wielkości.

        Args:
            df (pd.DataFrame): DataFrame zawierający kolumny Latitude, Longitude i kolumnę wielkości.
            size_col (str): Nazwa kolumny określającej wielkość bąbelków.
            template (str): Nazwa szablonu Plotly do zastosowania.

        Returns:
            plotly.graph_objects.Figure: Mapa bąbelkowa.

        Generates a bubble map based on location and size data.

        Args:
            df (pd.DataFrame): DataFrame containing Latitude, Longitude, and size column.
            size_col (str): Name of the column specifying the size of the bubbles.
            template (str): Name of the Plotly template to apply.

        Returns:
            plotly.graph_objects.Figure: Bubble map.
        """
    return px.scatter_geo(df, lat='Latitude', lon='Longitude', size=size_col,
                          color="Location", hover_name="Location",
                          projection="natural earth", title='Bubble Map', template=template)


