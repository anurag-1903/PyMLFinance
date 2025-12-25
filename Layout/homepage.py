from dash import html
import dash_bootstrap_components as dbc


def get_navigation_bar():
    navbar = dbc.NavbarSimple(
        brand=html.Span([
            html.Img(src=r"/assets/logo.png", height="65px", className="me-2"),
            "PyMLFinance"
            ]),
        color="#00414F",
        dark=True,
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/home", className="me-5", style={"color": "white"})),
            dbc.NavItem(dbc.NavLink("Courses", href="/courses", className="me-5", style={"color": "white"})),
            dbc.NavItem(dbc.NavLink("Resources", href="/resources", className="me-5", style={"color": "white"})),
            dbc.NavItem(dbc.NavLink("My Learning", href="/mylearning", className="me-5", style={"color": "white"})),
        ]
    )

    return navbar


def hero_section():
    return html.Div([
        dbc.Row([
            dbc.Col([
                html.H1("Python Machine Learning for Finance",
                        style={"color": "white"},className="display-5 fw-bold text-white"),
                html.P("Hands-on. Gamified. Data-Driven.",
                        style={"color":"white"}),
                dbc.Button("Get Started", color="#00414F",
                           style={"backgroundColor":"teal", "color":"white"})
                ],style={"padding":"50px"}),
            dbc.Col([
                html.Img(
                    src="assets/stock-market-candlestick.webp",
                    style={"width":"70%", "height":"auto"})
            ])
        ],style={"padding":"50px"})
    ], style={"backgroundColor":"#00414F"})


def cards_section():
    return html.Div([
        html.H1("Our Key Topics", className="text-center"),
        dbc.Row([
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H2("Python"),
                        html.P("a")
                    ], style={"backgroundColor": "teal", "color":"white"})
                ])
            ),
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H2("Machine Learning"),
                        html.P("b")
                    ], style={"backgroundColor": "teal", "color":"white"})
                ])
            ),
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H2("Finance"),
                        html.P("c")
                    ], style={"backgroundColor": "teal", "color":"white"})
                ])
            )
        ],style={"padding":"80px"})
    ],style={"backgroundColor":"#00414F", "color":"white"})

def courses_section():
    return html.Div([
        html.H2("Explore Our Courses", className="text-center"),
        dbc.Row([
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Python for Finance"),
                        html.P("Learn Python programming for finance."),
                        dbc.Button("View Course", color="teal", style={"backgroundColor": "#00414F", "color":"white"})
                    ], style={"backgroundColor": "teal", "color":"white"})
                )
            ),

            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.H4("Machine Learning for Finance"),
                        html.P("Learn machine learning with finance."),
                        dbc.Button("View Course", color="teal", style={"backgroundColor": "#00414F", "color":"white"})
                    ], style={"backgroundColor": "teal", "color":"white"})
                )
            )
        ], style={"padding": "80px"})
    ],style={"backgroundColor":"#00414F", "color":"white"})


def testimonial_section():
    return html.Div([
        html.H2("What Our Learners Say", className="text-center"),

        dbc.Row([
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.H6("- Anurag Choudhury", className="text-center", style={"fontStyle": "italic"}),
                        html.P(
                            "This course gave me a solid foundation in finance and Python. I was able to apply what i learned to my job immediately",
                            style={"fontSize": "16px"})
                    ], style={"backgroundColor": "teal", "color":"white"})
                )
            ),
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.H6("- Amrita Choudhury", className="text-center", style={"fontStyle": "italic"}),
                        html.P(
                            "The project were fun. I gained hands-on experience with real financial datasets",
                            style={"fontSize": "16px"})
                    ], style={"backgroundColor": "teal", "color":"white"})
                )
            ),
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.H6("- Sudish Kumar", className="text-center", style={"fontStyle": "italic"}),
                        html.P(
                            "The course covered a wide range of topics. I now feel confident in using Python for financial analysis",
                            style={"fontSize": "16px"})
                    ], style={"backgroundColor": "teal", "color":"white"})
                )
            )
        ],style={"padding":"80px"})
    ], style={"backgroundColor": "#00414F", "color": "white"})

