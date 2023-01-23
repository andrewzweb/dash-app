from dash import dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd


class Chart:
    def __init__(self, df):
        self.df = df
        self.prepare()

    def prepare(self):
        figure = px.bar(self.df, x="country", y="lifeExp", barmode="group")
        self.figure = figure

    def render(self):
        return dbc.Row(
            [dcc.Graph(id="world_chart", figure=self.figure)]  # fig_chart_lifeExp
        )
