import dash
from dash import Input, Output, State
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from callbacks.map_helpers import generate_scatter_map, generate_heatmap, generate_bubble_map

def register_visualization_callbacks(app):
    """
    Rejestruje callbacki związane z wizualizacją danych w aplikacji Dash.
    Registers callbacks related to data visualization in the Dash application.
    """
    @app.callback(
        Output('graph-output', 'figure'),
        [Input('bar-chart', 'n_clicks'),
         Input('pie-chart', 'n_clicks'),
         Input('line-chart', 'n_clicks'),
         Input('scatter-plot', 'n_clicks'),
         Input('area-chart', 'n_clicks'),
         Input('scatter-map', 'n_clicks'),
         Input('heatmap', 'n_clicks'),
         Input('bubble-map', 'n_clicks')],
        [State('template-dropdown', 'value'),
         State('stored-data', 'data')]
    )
    def render_charts(bar_clicks, pie_clicks, line_clicks, scatter_clicks, area_clicks, scatter_map_clicks, heatmap_clicks, bubble_map_clicks, template, data):
        """
                Callback do renderowania różnych typów wykresów na podstawie kliknięć użytkownika.
                Callback to render different types of charts based on user clicks.

                Args:
                    bar_clicks (int): Liczba kliknięć przycisku wykresu słupkowego.
                                      Number of clicks on the bar chart button.
                    pie_clicks (int): Liczba kliknięć przycisku wykresu kołowego.
                                      Number of clicks on the pie chart button.
                    line_clicks (int): Liczba kliknięć przycisku wykresu liniowego.
                                       Number of clicks on the line chart button.
                    scatter_clicks (int): Liczba kliknięć przycisku wykresu punktowego.
                                          Number of clicks on the scatter plot button.
                    area_clicks (int): Liczba kliknięć przycisku wykresu powierzchniowego.
                                       Number of clicks on the area chart button.
                    scatter_map_clicks (int): Liczba kliknięć przycisku mapy punktowej.
                                              Number of clicks on the scatter map button.
                    heatmap_clicks (int): Liczba kliknięć przycisku mapy cieplnej.
                                          Number of clicks on the heatmap button.
                    bubble_map_clicks (int): Liczba kliknięć przycisku mapy bąbelkowej.
                                             Number of clicks on the bubble map button.
                    template (str): Nazwa szablonu Plotly do zastosowania.
                                    Name of the Plotly template to apply.
                    data (list): Dane przechowywane w dcc.Store.
                                 Data stored in dcc.Store.

                Returns:
                    plotly.graph_objects.Figure: Wygenerowany wykres.
                                                 Generated chart.
                """
        ctx = dash.callback_context
        if not ctx.triggered or not data:
            return {}

        df = pd.DataFrame(data)
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if button_id == 'bar-chart':
            fig = px.bar(df, x=df.columns[0], y=df.columns[1], title='Bar Chart', template=template)
        elif button_id == 'pie-chart':
            fig = px.pie(df, names=df.columns[0], values=df.columns[1], title='Pie Chart', template=template)
        elif button_id == 'line-chart':
            fig = px.line(df, x=df.columns[0], y=df.columns[1], title='Line Chart', template=template)
        elif button_id == 'scatter-plot':
            fig = px.scatter(df, x=df.columns[0], y=df.columns[1], title='Scatter Plot', template=template)
        elif button_id == 'area-chart':
            fig = px.area(df, x=df.columns[0], y=df.columns[1], title='Area Chart', template=template)
        elif button_id == 'scatter-map':
            fig = generate_scatter_map(df, template)
        elif button_id == 'heatmap':
            fig = generate_heatmap(df, template)
        elif button_id == 'bubble-map':
            fig = generate_bubble_map(df, df.columns[2], template)
        else:
            fig = {}

        return fig

    @app.callback(
        Output('table-output', 'data'),
        Output('table-output', 'columns'),
        Output('table-output', 'style_table'),
        Input('table', 'n_clicks'),
        State('stored-data', 'data')
    )
    def render_table(table_clicks, data):
        """
                Callback do renderowania tabeli na podstawie danych przechowywanych w dcc.Store.
                Callback to render a table based on data stored in dcc.Store.

                Args:
                    table_clicks (int): Liczba kliknięć przycisku tabeli.
                                        Number of clicks on the table button.
                    data (list): Dane przechowywane w dcc.Store.
                                 Data stored in dcc.Store.

                Returns:
                    tuple: Przetworzone dane, kolumny i styl tabeli do wyświetlenia.
                           Processed data, columns, and table style to be displayed.
                """
        if table_clicks and data:
            df = pd.DataFrame(data)
            columns = [{'name': col, 'id': col} for col in df.columns]
            return df.to_dict('records'), columns, {'display': 'block'}
        return [], [], {'display': 'none'}