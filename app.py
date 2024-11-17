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
