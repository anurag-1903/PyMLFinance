from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from Layout.layout import get_layout
from Layout.coursepage import courses_page
from Layout.course_python import python_finance_page


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div([
    dcc.Location(id="url"),
    html.Div(id="page-content")
])

@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/courses":
        return courses_page()
    elif pathname == "/courses/python-finance":
        return python_finance_page()
    else:
        return get_layout()

if __name__ == "__main__":
    app.run(debug=True)
