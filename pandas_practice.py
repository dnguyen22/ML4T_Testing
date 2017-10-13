import pandas as pd


def test_read_csv():
    df = pd.read_csv('XOM.csv')
    print(df.head())

if __name__ == "__main__":
    test_read_csv()