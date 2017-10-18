"""Plot a histogram."""

import pandas as pd
import matplotlib.pyplot as plt
from util import get_data, plot_data, compute_daily_returns


if __name__ == "__main__":
    # Define date range
    start_date = '2015-09-15'
    end_date = '2017-10-05'
    # Read data
    dates = pd.date_range(start_date, end_date)
    symbols = ['SPY']
    df = get_data(symbols, dates)
    plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")

    # Plot a histogram
    daily_returns.hist(bins=5)
    plt.show()