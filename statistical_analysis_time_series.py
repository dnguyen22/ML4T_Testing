import pandas as pd  # Used for dataframes
import matplotlib.pyplot as plt  # Used for plotting
import os  # Used to get current working directory


def plot_data(df, title="Stock prices"):
    """Plot stock prices"""
    ax = df.plot(title=title, fontsize=8)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
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


if __name__ == "__main__":
    # Define date range
    start_date = '2017-09-15'
    end_date = '2017-10-05'
    # Read data
    dates = pd.date_range(start_date, end_date)
    symbols = ['SPY', 'AAPL', 'FB', 'GLD', 'GOOG', 'XOM']
    df = get_data(symbols, dates)
    # Plot
    plot_data(normalize_data(df))