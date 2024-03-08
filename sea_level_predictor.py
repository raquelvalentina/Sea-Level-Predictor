import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    fig, ax = plt.subplots(figsize=(8, 6))
    df.plot(ax=ax, kind='scatter',ylabel='Sea Level (inches)', xlabel='Year', title='Rise in Sea Level', x=['Year'], y=['CSIRO Adjusted Sea Level'])

    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_values = np.arange(df['Year'].min(), 2051)
    y_values = slope * x_values + intercept
    ax.plot(x_values, y_values, color='red', linestyle='--', label='Line of Best Fit')

    filtered_df = df[df['Year'] >= 2000]
    slope2, intercept2, _, _, _ = linregress(filtered_df['Year'], filtered_df['CSIRO Adjusted Sea Level'])
    x_values2 = np.arange(2000, 2051)
    y_values2 = slope2 * x_values2 + intercept2
    ax.plot(x_values2, y_values2, color='blue', linestyle='--', label='Line of Best Fit (2000-2050)')


    ax.set_xticks(range(1850, 2076, 25))
    # Mostrar la leyenda

    plt.savefig('sea_level_plot.png')

    return plt.gca()