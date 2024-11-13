"""
Purpose: Use Python to create a continuous intelligence and 
interactive analytics dashboard using Shiny for Python with 
interactive charts from HoloViews Bokeh and Plotly Express.

Each Shiny app has two parts: 

- a user interface app_ui object (similar to the HTML in a web page) 
- a server function that provides the logic for the app (similar to JS in a web page).

"""
from shiny import App, ui
import shinyswatch

from mtcars_server import get_mtcars_server_functions
from mtcars_ui_inputs import get_mtcars_inputs
from mtcars_ui_outputs import get_mtcars_outputs


from util_logger import setup_logger

logger, logname = setup_logger(__name__)

app_ui = ui.page_navbar(
    shinyswatch.theme.journal(),
    ui.navset_card_underline()(
        "MT_Cars",
        ui.layout_sidebar(
            get_mtcars_inputs(),
            get_mtcars_outputs(),
        ),
    ),
    
    ui.navset_card_underline()(ui.a("About", href="https://github.com/HMas522")),
    ui.navset_card_underline()(ui.a("GitHub", href="https://github.com/HMas522/cintel-04-reactive")),
    ui.navset_card_underline()(ui.a("App", href="https://HMas522.shinyapps.io/cintel-04-reactive/")),
    ui.navset_card_underline()(ui.a("Examples", href="https://shinylive.io/py/examples/")),
    ui.navset_card_underline()(ui.a("Widgets", href="https://shiny.rstudio.com/py/docs/ipywidgets.html")),
    title=ui.h1("Hmas522 Dashboard"),
)


def server(input, output, session):
    """Define functions to create UI outputs."""

    logger.info("Starting server...")
    
    get_mtcars_server_functions(input, output, session)
    

# app = App(app_ui, server, debug=True)
app = App(app_ui, server)