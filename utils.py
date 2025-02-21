#Basic Library
import numpy as np
import pandas as pd  # Make sure you have pandas imported

#Statistical Library
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller

#SkTime
from sktime.transformations.series.boxcox import BoxCoxTransformer

#Visualization
import matplotlib.pyplot as plt
import seaborn as sns 


def plot_multiple_lag_scatter(df, column, max_lag=3):
    """Create scatterplots for multiple lags of a time series with a diagonal reference line.

    Args:
        df (pandas.DataFrame): DataFrame containing the time series data.
        column (str): Name of the column to plot.
        max_lag (int, optional): Maximum number of lags to plot. Defaults to 3.

    Raises:
        KeyError: If `column` is not found in `df`.
        ValueError: If `max_lag` is less than 1 or exceeds the length of the DataFrame.

    Returns:
        None: Displays a matplotlib figure with subplots for each lag.

    Examples:
        >>> data = {'#Passengers': [112, 118, 132, 129, 121]}
        >>> df = pd.DataFrame(data)
        >>> plot_multiple_lag_scatter(df, '#Passengers', max_lag=3)
    """
    # Check if column exists
    if column not in df.columns:
        raise KeyError(f"Column '{column}' not found in DataFrame")
    # Validate max_lag
    if max_lag < 1:
        raise ValueError("max_lag must be a positive integer")
    if max_lag >= len(df):
        raise ValueError("max_lag must be less than the length of the DataFrame")

    #Extract the series
    series = df[column]

    #Create Figure with Subplots
    plt.figure(figsize=(15, 5))
    for i in range(1, max_lag + 1):
        plt.subplot(1, max_lag, i)
        series = df[column]
        lagged_series = series.shift(i)

        #Scatter plot of current vs lagged values 
        plt.scatter(series[i:], lagged_series[i:], alpha=0.5)
        # Add diagonal line (y=x)
        min_val = min(series.min(), lagged_series[i:].min())
        max_val = max(series.max(), lagged_series[i:].max())
        plt.plot([min_val, max_val], [min_val, max_val], 'r--', lw=1, label='y=x')

        # Labels and Title
        plt.xlabel(f'{column} (t)')
        plt.ylabel(f'{column} (t-{i})')
        plt.title(f'Lag {i}')
        plt.grid(True)
        plt.legend() # Show legend for the diagonal line
    plt.tight_layout()
    plt.show()




def plot_transformation(df, column = 'column'): 
    """Apply and visualize log and Box-Cox transformations on a time series.

    This function applies a logarithmic transformation and a Box-Cox transformation
    (with Guerrero method for lambda optimization) to the specified column in a DataFrame,
    then plots the original and transformed series for comparison.

    Args:
        df (pandas.DataFrame): DataFrame containing the time series data. The index should
            ideally be datetime for meaningful time series visualization.
        column (str, optional): Name of the column to transform and plot. Defaults to 'column'.

    Raises:
        KeyError: If `column` is not found in `df`.
        ValueError: If `df[column]` contains non-positive values (log and Box-Cox require
            positive data).
        ImportError: If `sktime` is not installed (required for BoxCoxTransformer).

    Returns:
        None: Displays a matplotlib figure with three subplots and adds transformed columns
            (`Log_{column}` and `BoxCox_{column}`) to `df`.

    Examples:
        >>> data = {'#Passengers': [112, 118, 132, 129, 121]}
        >>> df = pd.DataFrame(data, index=pd.to_datetime(['1949-01', '1949-02', '1949-03', '1949-04', '1949-05'], format='%Y-%m'))
        >>> plot_transformation(df, column='#Passengers')

    Notes:
        - The log transformation uses `np.log` (natural logarithm).
        - The Box-Cox transformation uses `sktime`'s `BoxCoxTransformer` with the Guerrero method
          and a seasonal period (`sp`) of 12 (assumes monthly data with yearly seasonality).
        - Ensure `df[column]` contains strictly positive values to avoid errors.
    """
    # Check if column exists in DataFrame
    if column not in df.columns:
        raise KeyError(f"Column '{column}' not found in DataFrame")

    # Check for non-positive values
    if (df[column] <= 0).any():
        raise ValueError(f"Column '{column}' contains non-positive values, which are invalid for log and Box-Cox transformations")
    
    #Apply Log Transformation
    df[f'Log_{column}'] = np.log(df[column])

    #Apply BoxCox with "Guerrero" Optimization to find optimal Lambda
    Transformer = BoxCoxTransformer(method = 'guerrero', sp= 12)
    df[f'BoxCox_{column}'] = Transformer.fit_transform(df[column])

    #Plot the original and transformed series 
    fig, axes = plt.subplots(3, 1, figsize=(10,8), sharex= True)

    axes[0].plot(df.index, df[column], label = 'Original', color = 'blue')
    axes[0].set_title(f'Original {column} Data') 
    axes[0].legend()

    axes[1].plot(df.index, df[f'Log_{column}'], label = 'Log', color = 'red')
    axes[1].set_title('Log Transformation')
    axes[1].legend()

    axes[2].plot(df.index, df[f'BoxCox_{column}'], label = 'BoxCox', color = 'green')
    axes[2].set_title('Box-Cox Transformation')
    axes[2].legend()
    plt.tight_layout
    plt.show()



def plot_time_series_decomposition(df, column = 'column'):
    """Plots the original time series and its decomposition components (trend, seasonal, residual).

    Args:
        df: Pandas DataFrame containing the original time series data.  It should have
           a DateTimeIndex and a column (e.g., '#Passengers') representing the time series.
        decomposition: The result of a time series decomposition (e.g., from statsmodels.tsa.seasonal.seasonal_decompose).

    Returns:
        None. Displays the plot.
    """
    decomposition = seasonal_decompose(df[column], model = 'multiplicative', period = 12)

    fig, axes = plt.subplots(4, 1, figsize=(10, 10), sharex=True)

    axes[0].plot(df.index, df[column], label='Original', color='blue')
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


def unit_root_test(series):
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