from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

import plotly.express as px
import pandas as pd

from app import app, get_data
from components import nav, chart

df = get_data()


layout = dbc.Container(
    [
        nav.Nav(active="Chart").render(),
        html.H1("Chart"),
        chart.Chart(df).render(),
    ]
)
