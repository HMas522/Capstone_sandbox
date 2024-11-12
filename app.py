from pathlib import Path

import pandas

from shiny import reactive
from shiny.express import render, ui


@reactive.calc
def dat():
    infile = Path(__file__).parent / "C:\Users\Hayley\Capstone_sandbox\English_Premier_League_standings.csv"
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