import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from util import get_data, plot_data, normalize_data


if __name__ == "__main__":
    start_val = 1000000
    # Define date range
    start_date = '2015-10-02'
    end_date = '2017-10-17'
    symbols = ['SPY', 'XOM', 'GOOG', 'ALRM']
    allocs = [0.4, 0.4, 0.1, 0.1]

    # Read data
    dates = pd.date_range(start_date, end_date)
    symbols = ['SPY', 'ALRM', 'GOOG', 'XOM']
    df = get_data(symbols, dates)

    normed = normalize_data(df)
    alloced = normed*allocs
    pos_vals = alloced*start_val
    port_val = pos_vals.sum(axis=1)  # Portfolio values

    daily_rets = (port_val / port_val.shift(1)) - 1  # Normalize (compute daily returns)
    daily_rets = daily_rets.ix[1:]  # First row value is 0, so get rid of it

    # Compute statistics
    cumulative = (port_val[-1]/port_val[0]) - 1
    print("cumulative=", cumulative)
    mean = daily_rets.mean()
    print("Mean=", mean)
    std = daily_rets.std()
    print("st.dev=",std)
    # Calculate Sharpe ratio
    daily_rf = ((1.0+0.1) ** (1.0/252.0)) - 1  #  Daily risk-free rate can be approx. by 0
    sharpe = (daily_rets - daily_rf).mean()/(daily_rets - daily_rf).std()
    print("Sharpe ratio=", sharpe)
