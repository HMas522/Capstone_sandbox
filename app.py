from shiny.express import input, render, ui
from shinyswatch import theme

ui.page_opts(title="Hmass Dashboard", fillable=True)


from pathlib import Path

import pandas

from shiny import reactive
from shiny.express import render, ui

with ui.sidebar(open="desktop"):
    ui.h2("Sidebar")
    ui.tags.hr()
    ui.h3("Interaction")
    ui.input_text("name_input", "Enter your name", placeholder="Your Name")
    ui.input_text("language_input", "Enter your favorite language(s)", placeholder="Favorite Programming Language(s)")
    ui.tags.hr()
    ui.h3("Links")
    ui.a("PyShiny", href="https://shiny.posit.co/py/", target="_blank")
    ui.a("Examples", href="https://shinylive.io/py/examples/", target="_blank")
    ui.a("Themes", href="https://posit-dev.github.io/py-shinyswatch/", target="_blank")
    ui.a("Deploy", href="https://docs.posit.co/shinyapps.io/getting-started.html#working-with-shiny-for-python", target="_blank")
    ui.a("GitHub", href="https://github.com/denisecase", target="_blank")
    ui.a("GitHub Repository", href="https://github.com/denisecase/cintel-02-app", target="_blank")
    ui.a("Shinylive.io App", href="https://denisecase.shinyapps.io/cintel-02-app/", target="_blank")
   
with ui.layout_columns(fill=False):       
    ui.h2("Main Area with Reactive Output")
 
  
@render.text
def welcome_output():
    user = input.name_input();
    welcome_string = f'Greetings {user}!';
    return welcome_string

@reactive.calc
def dat():
    infile = Path(__file__).parent / "English_Premier_League_standings.csv"
    return pandas.read_csv(infile)


with ui.navset_card_underline():

    with ui.nav_panel("Data frame"):
        @render.data_frame
        def frame():
            # Give dat() to render.DataGrid to customize the grid
            return dat()

    with ui.nav_panel("Table"):
        @render.table
        def table():
            return dat()