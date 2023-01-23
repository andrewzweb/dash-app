from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app
from apps.app_pie import pie
from apps.app_chart import chart
from apps.main_page import main_page


app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/":
        return main_page.layout
    elif pathname == "/apps/pie":
        return pie.layout
    elif pathname == "/apps/chart":
        return chart.layout
    else:
        return "404"


if __name__ == "__main__":
    app.run_server(debug=True)
