import pandas as pd  # Used for dataframes
import matplotlib.pyplot as plt  # Used for plotting
from datetime import datetime


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
    # Create an empty dataframe
    df1 = pd.DataFrame(index=dates)

    # Read SPY data into temporary dataframe
    dfSPY = pd.read_csv('data/SPY.csv', index_col='Date',
                        parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])

    # Rename 'Adj Close' column with 'SPY' to prevent clash
    dfSPY = dfSPY.rename(columns={'Adj Close':'SPY'})

    # Join the two dataframes using DataFrame.join() with an inner join
    df1 = df1.join(dfSPY, how='inner')

    # Drop NaN values if an inner join was NOT used
    # df1 = df1.dropna()

    # Read in more stocks
    symbols = ['AAPL', 'FB', 'GLD', 'GOOG', 'XOM']
    for symbol in symbols:
        df_temp=pd.read_csv('data/{}.csv'.format(symbol), index_col='Date',
                            parse_dates=True, usecols=['Date', 'Adj Close'],
                            na_values=['nan'])

        # Rename to prevent clash
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df1 = df1.join(df_temp)  # Use default how='left'
    print(df1)


if __name__ == "__main__":
    data_frame = test_read_csv()
    """
    slice_data()
    print('Max close: ')
    print(get_max_close(data_frame))
    print('Mean volume: ')
    print(get_mean_volume(data_frame))
    plot_adj_close(data_frame)
    """
    date_range()

