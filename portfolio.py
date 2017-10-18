import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from util import get_data, plot_data, compute_daily_returns, normalize_data


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
    port_val = pos_vals.sum(axis=1)