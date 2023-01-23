import dash
import dash_bootstrap_components as dbc
import pandas as pd

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


def get_data():
    dtypes = {
        "continent": "str",
        "country": "str",
        "pop": "float32",
        "lifeExp": "float32",
    }
    df = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv",
        dtype=dtypes,
    )
    return df[["continent", "country", "pop", "lifeExp"]]


server = app.server
app.config.suppress_callback_exceptions = True
