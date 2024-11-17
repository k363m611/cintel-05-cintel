# --------------------------------------------
# Imports at the top - PyShiny EXPRESS VERSION
# --------------------------------------------

# From shiny, import just reactive and render
from shiny import reactive, render

# From shiny.express, import just ui
from shiny.express import ui

# Imports from Python Standard Library to simulate live data
import random
from datetime import datetime

# --------------------------------------------
# Optional: Import font awesome icons as you like
# --------------------------------------------

from faicons import icon_svg

# --------------------------------------------
# FOR OPTIONAL LOCAL DEVELOPMENT
# --------------------------------------------

# Add all packages not in the Std Library
# to requirements.txt ONLY when working locally:
#
# faicons
# shiny
# shinylive
#
# And install them into an active project virtual environment (usually in .venv)
# --------------------------------------------


# --------------------------------------------
# SET UP THE REACTIVE CONTENT
# --------------------------------------------

# First, set a constant UPDATE INTERVAL for all live data
UPDATE_INTERVAL_SECS: int = 1

# Initialize a REACTIVE CALC that will get the fake temperature and timestamp every N seconds
@reactive.calc()
def reactive_calc_combined():
    # Invalidate this calculation every UPDATE_INTERVAL_SECS to trigger updates
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)

    # Data generation logic. Get random temperature between -18 and -16 C, rounded to 1 decimal place
    temp = round(random.uniform(-18, -16), 1)

    # Get a timestamp for "now"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Return the fake data as a dictionary
    latest_dictionary_entry = {"temp": temp, "timestamp": timestamp}

    return latest_dictionary_entry


# --------------------------------------------
# Define the Shiny UI Page layout - Page Options
# --------------------------------------------

# Set the page title and enable the full-width layout
ui.page_opts(title="PyShiny Express: Live Data (Basic)", fillable=True)


# ------------------------------------------------
# Define the Shiny UI Page layout - Sidebar
# ------------------------------------------------
with ui.sidebar(open="open"):
    ui.h2("Antarctic Explorer", class_="text-center")
    ui.p(
        "A demonstration of real-time temperature readings in Antarctica.",
        class_="text-center",
    )


# ------------------------------------------------
# Define the Shiny UI Page layout - Main Content
# ------------------------------------------------

# Main content area - Current temperature
ui.h2("Current Temperature")

@render.text
def display_temp():
    """Get the latest reading and return a temperature string"""
    latest_dictionary_entry = reactive_calc_combined()
    return f"{latest_dictionary_entry['temp']} C"

# Optional Font Awesome icon (e.g., sun icon)
icon_svg("sun")

# Add a horizontal rule for styling
ui.hr()

# Main content area - Current Date and Time
ui.h2("Current Date and Time")

@render.text
def display_time():
    """Get the latest reading and return a timestamp string"""
    latest_dictionary_entry = reactive_calc_combined()
    return f"{latest_dictionary_entry['timestamp']}"
