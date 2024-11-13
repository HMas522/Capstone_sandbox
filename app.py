from pathlib import Path
import pandas as pd
from shiny import App, ui, render, reactive
import shinyswatch  # For themes

# Define the reactive data fetching function
@reactive.calc
def dat() -> pd.DataFrame:
    infile = Path(__file__).parent / "English_Premier_League_standings.csv"
    return pd.read_csv(infile)

# Define the UI with shinyswatch theme
app_ui = ui.page_navbar(
    shinyswatch.theme.journal(),  # Apply the journal theme from shinyswatch
    ui.navset_card_underline(  # Set up a tabbed navigation layout
        ui.nav_panel("Data frame", 
            ui.output_data_frame("frame")  # Output for the data frame tab
        ),
        ui.nav_panel("Table", 
            ui.output_table("table")  # Output for the table tab
        )
    )
)

# Define the server function
def server(input, output, session):
    # Render the data frame for the "Data frame" tab
    @output()
    @render.data_frame
    def frame() -> pd.DataFrame:
        return dat()
    
    # Render the table for the "Table" tab
    @output()
    @render.table
    def table() -> pd.DataFrame:
        return dat()

# Create the app
app = App(app_ui, server)

# Run the app
if __name__ == "__main__":
    app.run()