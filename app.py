# --------------------------------------------
# Imports at the top - PyShiny EXPRESS VERSION
# --------------------------------------------

from shiny import reactive, render
from shiny.express import ui
import random
from datetime import datetime
from faicons import icon_svg

# --------------------------------------------
# SET UP THE REACTIVE CONTENT
# --------------------------------------------

UPDATE_INTERVAL_SECS: int = 1  # Data update every 1 second

# Initialize a REACTIVE CALC to simulate fake temperature and timestamp data
@reactive.calc()
def reactive_calc_temperature():
    # Invalidate this calculation every UPDATE_INTERVAL_SECS to trigger updates
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)

    # Simulate temperature data (between -18 and -16 degrees Celsius)
    temp = round(random.uniform(-18, -16), 1)

    # Get a timestamp for "now"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Return the data as a dictionary
    latest_data_entry = {"temp": temp, "timestamp": timestamp}
    return latest_data_entry


# --------------------------------------------
# Define the Shiny UI Page layout - Page Options
# --------------------------------------------

ui.page_opts(title="Antarctic Temperature Tracker", fillable=True)

# Sidebar with fun information
with ui.sidebar(open="open"):
    ui.h2("🌨️ Antarctic Explorer 🐧", class_="text-center")
    ui.p(
        "A demo app to track the latest temperature in Antarctica. Stay warm or freeze! ❄️",
        class_="text-center",
    )
    ui.hr()
    ui.h6("Links:")
    ui.a("GitHub Source", href="https://github.com/k363m611", target="_blank")
    ui.a("PyShiny", href="https://shiny.posit.co/py/", target="_blank")

# ------------------------------------------------
# Main content area - Current Data
# ------------------------------------------------

# Main content - Current Temperature Box with fun icons
with ui.row():  # Use `ui.row()` for layout
    with ui.column():
        with ui.value_box(
            showcase=icon_svg("thermometer-half"),  # Icon representing temperature
            theme="bg-gradient-blue-purple",
        ):
            "Current Temperature"
            @render.text
            def display_temp():
                """Get the latest temperature reading"""
                latest_data_entry = reactive_calc_temperature()
                return f"{latest_data_entry['temp']}°C"

    with ui.column():
        with ui.value_box(
            showcase=icon_svg("calendar-alt"),  # Calendar icon for timestamp
            theme="bg-gradient-purple-pink",
        ):
            "Current Timestamp"
            @render.text
            def display_timestamp():
                """Get the latest timestamp"""
                latest_data_entry = reactive_calc_temperature()
                return f"{latest_data_entry['timestamp']}"

# ------------------------------------------------
# Optional: Add a chart to show temperature trends
# ------------------------------------------------

# This section could be expanded with a plotly chart (if you want a trendline)
# For simplicity, we'll just display the last N readings in a data grid.

# --------------------------------------------
# Display Most Recent Data Readings
# --------------------------------------------

with ui.card(full_screen=True):
    ui.card_header("📊 Most Recent Temperature Readings")
    @render.data_frame
    def show_data_frame():
        """Display the last few temperature readings in a table"""
        latest_data_entry = reactive_calc_temperature()
        # Here you could store and display the last few readings, but for now:
        df = pd.DataFrame([latest_data_entry])
        return render.DataGrid(df, width="100%", height=300)
