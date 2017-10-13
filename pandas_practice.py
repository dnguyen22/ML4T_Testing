import pandas as pd  # Used for dataframes
import matplotlib.pyplot as plt  # Used for plotting


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
    df['Adj Close'].plot()
    plt.show()  # Must be called to show plot


if __name__ == "__main__":
    data_frame = test_read_csv()
    """
    slice_data()
    print('Max close: ')
    print(get_max_close(data_frame))
    print('Mean volume: ')
    print(get_mean_volume(data_frame))
    """
    plot_adj_close(data_frame)
