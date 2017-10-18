import pandas as pd  # Used for dataframes
import matplotlib.pyplot as plt  # Used for plotting
import os  # Used to get current working directory


def fill_missing_values(df_data):
    """Fill missing values in data frame, in place."""
    df_data.fillna(method='ffill', inplace=True)  # Forward fill NaN values with last valid value
    df_data.fillna(method='bfill', inplace=True)  # Back fill NaN values with newest valid value


def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):
    """Plot stock prices"""
    ax = df.plot(title=title, fontsize=8)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()  # Must be called to show plots in some environments


def get_data(symbols, dates):
    """Read stock data (adjusted close for given symbols from CSV files."""
    # Create an empty dataframe
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # Add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    # Read and join data for each symbol
    for symbol in symbols:
        df_temp=pd.read_csv(symbol_to_path(symbol), index_col='Date',
                            parse_dates=True, usecols=['Date', 'Adj Close'],
                            na_values=['nan'])

        # Rename to prevent clash
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)  # Use default how='left'
        if symbol == 'SPY':  # Drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])

    return df


def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def normalize_data(df):
    """Normalize stock prices using the first row of the dataframe."""
    return df/df.ix[0,:]


def get_bollinger_bands(rm, rstd):
    """Return upper and lower Bollinger Bands. Mean +/- 2 standard deviations"""
    upper_band = rm + rstd * 2
    lower_band = rm - rstd * 2
    return upper_band, lower_band


def compute_daily_returns(df):
    """Compute and return the daily return values."""
    daily_ret = df.copy()  # Copy given data frame to match size and column names
    # Compute daily returns for row 1 onwards
    #daily_ret[1:] = (df[1:] / df[:-1].values) - 1  # Alternative method using numpy
    daily_ret = (df / df.shift(1)) - 1
    daily_ret.ix[0, :] = 0  # Set daily returns for row 0 to 0
    return daily_ret