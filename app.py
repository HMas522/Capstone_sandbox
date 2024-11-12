
from shiny.express import input, render, ui
from shinyswatch import theme

ui.page_opts(title="Hmass Dashboard", fillable=True)
 theme.journal()
# theme.cerulean()

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
    
   
with ui.layout_columns(fill=False):       
    ui.h2("Main Area with Reactive Output")
 
  
@render.text
def welcome_output():
    user = input.name_input()
    welcome_string = f'Greetings {user}!'
    return welcome_string


@render.text
def insights_output():
    answer = input.language_input()
    count = len(answer)
    language_string = f'You like {answer}. That takes {count} characters'
    return language_string