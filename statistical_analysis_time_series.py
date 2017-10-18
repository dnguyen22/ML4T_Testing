import pandas as pd  # Used for dataframes
import matplotlib.pyplot as plt  # Used for plotting
import os  # Used to get current working directory


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


def print_global_stats(df):
    print(df.mean())
    print(df.median())
    print(df.std())


def rolling_mean_demo(df):
    # Compute rolling mean using a 3-day window
    #rm_SPY = pd.rolling_mean(df['SPY'], window=20)  # Old method
    #rm_SPY = df['SPY'].rolling(window=3, center=False).mean()

    # Compute Bollinger Bands
    # 1. Compute rolling mean
    rm_SPY = get_rolling_mean(df['SPY'], window=20)

    # 2. Compute rolling standard deviation
    rstd_SPY = get_rolling_std(df['SPY'], window=20)

    # 3. Compute upper and lower bands
    upper_band, lower_band = get_bollinger_bands(rm_SPY, rstd_SPY)

    # Plot raw SPY data, rolling mean and Bollinger Bands
    ax = df['SPY'].plot(title="Bollinger Bands", label='SPY')
    # Add rolling mean to same plot
    rm_SPY.plot(label='Rolling mean', ax=ax)
    upper_band.plot(label='upper band', ax=ax)
    lower_band.plot(label='lower band', ax=ax)

    # Add axis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()


def get_rolling_mean(values, window):
    """Return rolling mean of given values, using specified window"""
    return values.rolling(window=window, center=False).mean()


def get_rolling_std(values, window):
    """Return rolling standard deviation of given values, using specified window"""
    return values.rolling(window=window, center=False).std()


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


def fill_missing_values(df_data):
    """Fill missing values in data frame, in place."""
    df_data.fillna(method='ffill', inplace=True)  # Forward fill NaN values with last valid value
    df_data.fillna(method='bfill', inplace=True)  # Back fill NaN values with newest valid value


if __name__ == "__main__":
    # Define date range
    start_date = '2015-09-15'
    end_date = '2017-10-05'
    # Read data
    dates = pd.date_range(start_date, end_date)
    symbols = ['SPY', 'ALRM', 'GOOG', 'XOM']
    df = get_data(symbols, dates)

    # Fill missing values
    fill_missing_values(df)

    # Plot
    plot_data(normalize_data(df))

    # Compute global statistics for each stock
    #print_global_stats(df)

    rolling_mean_demo(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")
