from pathlib import Path
import pandas as pd
from shiny import App, ui, render, reactive


# Define the reactive data fetching function
@reactive.calc
def dat() -> pd.DataFrame:
    infile = Path(__file__).parent / "English_Premier_League_standings.csv"
    return pd.read_csv(infile)

# Define the UI using the shinyswatch theme
app_ui = ui.page_navbar(
    ui.navset_card_underline(
        ui.nav_panel("Data frame", 
            ui.output_data_frame("frame")
        ),
        ui.nav_panel("Table", 
            ui.output_table("table")
        )
    )
)

# Define the server function
def server(input, output, session):
    
    @output()
    @render.data_frame
    def frame() -> pd.DataFrame:
        return dat()
    
    @output()
    @render.table
    def table() -> pd.DataFrame:
        return dat()

# Create the app
app = App(app_ui, server)

# Run the app
if __name__ == "__main__":
    app.run()