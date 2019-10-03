import ClimateInput as CI
import ClimateProcessing as CP
import matplotlib.pyplot as plt
import pandas as pd

# Get user input
cityInput = CI.cityInput()
fieldList = CI.fieldInput()
plotInput = CI.plotInput()

# Process Data
cityData = CP.processData(cityInput, fieldList)

monthlyData = cityData.groupby(cityData.index.month).mean()
dailyDataAVG = cityData.groupby([cityData.index.month, cityData.index.day]).mean()
dailyDataMin = cityData.groupby([cityData.index.month, cityData.index.day]).min()
dailyDataMax = cityData.groupby([cityData.index.month, cityData.index.day]).max()
ghiData = cityData.groupby(cityData.index.hour).mean()

# Display plots
monthlyData.plot(title='Monthly')
dailyDataAVG.plot(title='Daily Data Average')
dailyDataMin.plot(title='Daily Data Minimum')
dailyDataMax.plot(title='Daily Data Maximum')
ghiData.plot(title='GHI Hourly Data')
plt.show()
