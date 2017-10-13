import pandas as pd


def test_read_csv():
    df = pd.read_csv('XOM.csv')
    print(df.head())  # Prints first 5 rows of data
    print(df.tail())  # Prints last 5 rows of data


def slice_data():
    df = pd.read_csv('XOM.csv')
    print(df[10:16])  # Prints rows index 10, 11, 12, 13, 14 and 15


if __name__ == "__main__":
    # test_read_csv()
    slice_data()
