from dash import html
import dash_bootstrap_components as dbc
from Layout.homepage import get_navigation_bar

def python_finance_page():
    return html.Div([
        get_navigation_bar(),

        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H1("Python for Finance", className="bold text-white"),
                    html.P("Learn Python programming with real-world financial datasets.", className="text-white"),
                    dbc.Button("Enroll Now", color="teal", style={"backgroundColor": "teal"})
                ]),

                dbc.Col([
                    html.Img(src="/assets/stock-market-candlestick.webp",
                             style={"width": "70%"})
                ])
            ])
        ],style={"padding":"50px"}),

        dbc.Container([
            html.H3("Course Overview", className="text-white"),
            html.P(
                "This course is designed to teach you Python programming with a strong focus on finance. "
                , className="text-white")
        ],style={"padding":"50px"}),

        dbc.Container([
            dbc.Row([
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H5("Module 1: Python Basics")
                        ], style={"backgroundColor": "teal"})
                    )
                ),

                dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H5("Module 2: Data Analysis")
                        ], style={"backgroundColor": "teal"})
                    )
                ),

                dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H5("Module 3: Visualization")
                        ], style={"backgroundColor": "teal"})
                    )
                )
            ], align="center")
        ],style={"padding":"50px"}),

        dbc.Container([
            html.Div([
                html.H3("Ready to start learning?", className="fw-bold text-center text-white"),
                dbc.Button("Enroll in Python for Finance", color="teal",
                            className="text-center text-black", style={"backgroundColor": "teal"})
            ])
        ],style={"padding":"50px"})
    ], style={"backgroundColor": "#00414F"})
