import os
import pandas as pd


def processData(city):
    filepath = 'Cities/' + city + '.CSV'
    cityData = pd.read_csv(filepath)

    cityData = cityData.filter['Date (MM/DD/YYYY)', 'Time (HH:MM)','GHI (W/m^2)', 'Dry-bulb (C)', 'Dew-point (C)', 'RHum (%)', 'Wspd (m/s)']
    print(cityData.dtypes)
