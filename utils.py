import matplotlib.pyplot as plt
import pandas as pd  # Make sure you have pandas imported
from statsmodels.tsa.stattools import adfuller

def plot_time_series_decomposition(df, decomposition):
    """Plots the original time series and its decomposition components (trend, seasonal, residual).

    Args:
        df: Pandas DataFrame containing the original time series data.  It should have
           a DateTimeIndex and a column (e.g., '#Passengers') representing the time series.
        decomposition: The result of a time series decomposition (e.g., from statsmodels.tsa.seasonal.seasonal_decompose).

    Returns:
        None. Displays the plot.
    """

    fig, axes = plt.subplots(4, 1, figsize=(10, 10), sharex=True)

    axes[0].plot(df.index, df['#Passengers'], label='Original', color='blue')
    axes[0].set_title('Original AirPassengers Data')
    axes[0].legend()

    axes[1].plot(df.index, decomposition.trend, label='Trend', color='green')
    axes[1].set_title('Trend Component')
    axes[1].legend()

    axes[2].plot(df.index, decomposition.seasonal, label='Seasonal', color='orange')
    axes[2].set_title('Seasonal Component')
    axes[2].legend()

    axes[3].plot(df.index, decomposition.resid, label='Residual', color='red')
    axes[3].set_title('Residual Component')
    axes[3].legend()

    plt.tight_layout()
    plt.show()


def adf_test(series):
    result = adfuller(series)
    print('ADF Statistic: %f' % result[0])
    print('p-value: %f' % result[1])
    print('Critical Values: %s' % result[4])
    if result[1] > 0.05:
        print('Series is likely non-stationary')
        return False  # Non-stationary
    else:
        print('Series is likely stationary')
        return True  # Stationary