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

# Display plots
for field in fieldList:
    cityData.plot(y=field, color='red')

plt.show()
