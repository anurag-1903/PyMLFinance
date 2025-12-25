from Layout.homepage import get_navigation_bar, hero_section, cards_section, courses_section,testimonial_section
from dash import html


def get_layout():
    return  html.Div([
        get_navigation_bar(),
        hero_section(),
        cards_section(),
        courses_section(),
        testimonial_section()
    ])




