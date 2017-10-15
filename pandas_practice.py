import pandas as pd  # Used for dataframes
import matplotlib.pyplot as plt  # Used for plotting
import os


def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


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


def test_read_csv():
    df = pd.read_csv('XOM.csv')
    """
    print(df.head())  # Prints first 5 rows of data
    print(df.tail())  # Prints last 5 rows of data
    """
    return df


def slice_data():
    df = pd.read_csv('XOM.csv')
    print(df[10:16])  # Prints rows index 10, 11, 12, 13, 14 and 15


def get_max_close(df):
    """Return the maximum closing value.

    """
    return df['Close'].max()


def get_mean_volume(df):
    """Return the mean volume value.

    """
    return df['Volume'].mean()


def plot_adj_close(df):
    """Plots the adj close value.

    """
    df[['High', 'Adj Close']].plot()
    plt.show()  # Must be called to show plot


def date_range():
    """Creates dataframe with dates as index.

    """
    # Define date range
    start_date = '2017-09-15'
    end_date = '2017-10-05'
    dates = pd.date_range(start_date, end_date)

    # Drop NaN values if an inner join was NOT used
    # df1 = df1.dropna()

    # Read in more stocks
    symbols = ['AAPL', 'FB', 'GLD', 'GOOG', 'XOM']

    # Get stock data
    df = get_data(symbols, dates)

    # Slice by row ranges (dates) using DataFrame.ix[] selector
    #print(df.ix['2017-09-20':'2017-09-30'])

    # Slice by column (symbols)
    #print(df['GOOG'])  # A single label selects a single column
    #print(df[['AAPL', 'XOM']])  # A list of labels selects multiple columns

    # Slice by row and column
    print(df.ix['2017-09-20':'2017-09-30', ['SPY', 'XOM']])


if __name__ == "__main__":

    """
    data_frame = test_read_csv()
    slice_data()
    print('Max close: ')
    print(get_max_close(data_frame))
    print('Mean volume: ')
    print(get_mean_volume(data_frame))
    plot_adj_close(data_frame)
    """
    date_range()

