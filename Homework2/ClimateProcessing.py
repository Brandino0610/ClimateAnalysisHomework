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

    # Conversion of datetimes
    mapping = {'01:00': '00:00', '02:00': '01:00', '03:00': '02:00', '04:00': '03:00',
               '05:00': '04:00', '06:00': '05:00', '07:00': '06:00', '08:00': '07:00',
               '09:00': '08:00', '10:00': '09:00', '11:00': '10:00', '12:00': '11:00',
               '13:00': '12:00', '14:00': '13:00', '15:00': '14:00', '16:00': '15:00',
               '17:00': '16:00', '18:00': '17:00', '19:00': '18:00', '20:00': '19:00',
               '21:00': '20:00', '22:00': '21:00', '23:00': '22:00', '24:00': '23:00'}

    cityData['Time (HH:MM)'] = cityData['Time (HH:MM)'].replace(mapping)

    # Make a list of datetime for x-axis
    datetimelist = cityData['Date (MM/DD/YYYY)'] + ' ' + cityData['Time (HH:MM)']

    # Convert List to datetime
    datetimelist = pd.to_datetime(datetimelist)

    # Replace original date and time columns into dataframe index
    cityData = cityData.drop(columns=['Time (HH:MM)', 'Date (MM/DD/YYYY)'])
    cityData = cityData.set_index(datetimelist)
    cityData.columns = ['ghi', 'drybulbtemp', 'dewpoint', 'relativehumidity', 'windspeed']

    return cityData