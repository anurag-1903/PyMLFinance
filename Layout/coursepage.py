from dash import html
import dash_bootstrap_components as dbc
from Layout.homepage import get_navigation_bar

def courses_page():
    return html.Div([
        get_navigation_bar(),

        html.Div([
            html.H1("Explore Our Courses", className="bold text-center text-white"),
            html.P("Choose from beginner to advanced courses in Python, Machine Learning, and Finance.",
                   className="text-center text-white")
        ], style={"backgroundColor": "#00414F"}),

        dbc.Container([
            dbc.Row([
                dbc.Col(
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Python for Finance", className="card-title"),
                            html.P("Learn Python programming with real-world financial datasets."),
                            dbc.Button("View Details", color="teal", href="/courses/python-finance",
                                       style={"backgroundColor":"#00414F", "color":"white"})
                        ], style={"backgroundColor": "teal"})
                    ])
                ),

                dbc.Col(
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Machine Learning for Finance", className="card-title"),
                            html.P("Understand ML in finance."),
                            dbc.Button("View Details", color="teal", href="/courses/ml-finance",
                                       style={"backgroundColor":"#00414F", "color":"white"})
                        ], style={"backgroundColor": "teal"})
                    ])
                ),

                dbc.Col(
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Finance", className="card-title"),
                            html.P("Finance with Python and ML."),
                            dbc.Button("View Details", color="teal", href="/courses/quant-trading",
                                       style={"backgroundColor":"#00414F", "color":"white"})
                        ], style={"backgroundColor": "teal"})
                    ])
                ),

            ])
        ], style={"backgroundColor": "#00414F", "padding": "60px"}),

        html.Div([
            html.H2("Not sure where to start?", className="text-center text-white"),
            html.P("Check out our beginner-friendly Python for Finance course to get started.",
                   className="text-center text-white"),
            dbc.Button("Start with Python for Finance", href="/courses/python-finance",
                       color="light", className="text-center")
        ], style={"padding": "60px"})
    ], style={"backgroundColor": "#00414F"})
