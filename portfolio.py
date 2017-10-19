import pandas as pd
import math
from util import get_data, normalize_data


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
    print("Cumulative Return=", cumulative)
    mean = daily_rets.mean()
    print("Average Daily Return (Mean)=", mean)
    std = daily_rets.std()
    print("Risk (St.Dev)=",std)
    # Calculate Sharpe ratio
    daily_rf = ((1.0+0.1) ** (1.0/252.0)) - 1  #  Daily risk-free rate can be approx. by 0
    sharpe = (daily_rets - daily_rf).mean()/(daily_rets - daily_rf).std()
    k = math.sqrt(252)  # Sharpe correction factor for non-annual values. Equals sqrt of samples per year
    sharpe_annualized = sharpe * k
    print("Sharpe Ratio=", sharpe_annualized)
