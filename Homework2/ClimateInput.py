import os


def cityInput():
    cities = ('anchorage', 'dallas', 'guam', 'losangelos', 'miami', 'newyork')
    print(os.listdir('Cities'))
    response = input("Enter a city listed above: ").lower()
    while response not in cities:
        response = input("Invalid Response! Please enter a city listed above: ").lower()

    return response


def fieldInput():
    fields = ('dewpoint', 'drybulbtemp', 'ghi', 'relativehumidity', 'windspeed')
    print(fields)
    response = input("Enter the fields to be plotted: ")

    return response


def plotInput():
    plots = ('scatterplot', 'monthlytemp', 'hourvalues')
    print(plots)
    response = input("Enter a plot above: ")

    return response

