import os
import pandas as pd
from datetime import timedelta

def processData(city, fields):

    # Create filepath from city argument
    filepath = 'Cities/' + city + '.CSV'

    # Parse data in file to panda dataframe
    cityData = pd.read_csv(filepath)

    # Strip down data to only needed fields
    cityData = cityData[['Date (MM/DD/YYYY)', 'Time (HH:MM)','GHI (W/m^2)', 'Dry-bulb (C)', 'Dew-point (C)', 'RHum (%)', 'Wspd (m/s)']]

    # Fix hour formatting
    cityData['Time (HH:MM)'] = cityData['Time (HH:MM)'].replace('24:00', '00:00')

    # Make a list of datetime for x-axis
    datetimelist = cityData['Date (MM/DD/YYYY)'] + ' ' + cityData['Time (HH:MM)']

    # Convert List to datetime
    datetimelist = pd.to_datetime(datetimelist) - timedelta(hours=1)

    # Replace original date and time columns into dataframe index
    cityData = cityData.drop(columns=['Time (HH:MM)', 'Date (MM/DD/YYYY)'])
    cityData = cityData.set_index(datetimelist)

    return cityData