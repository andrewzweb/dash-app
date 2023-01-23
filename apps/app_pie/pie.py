from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import plotly.express as px
import pandas as pd

from app import app, get_data
from components.nav import Nav


layout = dbc.Container(
    [
        Nav(active="Pie").render(),
        html.H1("Pie Chart"),
        dcc.Graph(id="graph"),
        html.P("Filter by continent:"),
        dcc.Dropdown(
            id="continent",
            options=["Africa", "Asia", "Europe", "Americas", "Oceania"],
            value="Europe",
        ),
        html.P("Values:"),
        dcc.Dropdown(id="sort_by", options=["pop", "lifeExp"], value="pop"),
    ]
)


@app.callback(
    Output("graph", "figure"), Input("sort_by", "value"), Input("continent", "value")
)
def generate_chart(sort_by, continent):
    df = get_data()
    df = px.data.gapminder().query(f"continent == '{continent}'")
    fig = px.pie(
        df,
        values=sort_by,
        names="country",
        title=f"Population in {continent}",
        hover_data=["lifeExp"],
        labels={"lifeExp": "life expectancy"},
    )
    return fig
