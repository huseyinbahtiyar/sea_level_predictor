import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
def draw_plot():
    # Read data from file
    df=pd.read_csv("epa-sea-level.csv")
    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']
    x2=np.arange(1880,2051)
    x3=np.arange(2000,2051)
    df2=df[df['Year']>=2000]
    # Create scatter plot
    plt.scatter(x,y)

    # Create first line of best fit
    res = linregress(x, y)
    plt.plot(x2, res.intercept + res.slope*x2, 'r', label='fitted line')

    # Create second line of best fit
    res2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    plt.plot(x3, res2.intercept + res2.slope*x3, 'r--', label='fitted line')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()