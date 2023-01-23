from dash import dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd


class Map:
    def __init__(self):
        self.prepare()

    def prepare(self):
        # df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
        # df = df[['continent', 'country', 'pop', 'lifeExp']]

        df = px.data.gapminder().query("year == 2007")
        fig_world = px.scatter_geo(
            df,
            locations="iso_alpha",
            color="continent",
            hover_name="country",
            size="pop",
            projection="natural earth",
        )
        self.figure = fig_world

    def render(self):
        return dbc.Row(
            [dcc.Graph(id="world_map", figure=self.figure)]  # fig_chart_lifeExp
        )
