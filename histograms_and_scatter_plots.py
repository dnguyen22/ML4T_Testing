"""Plot a histogram."""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from util import get_data, plot_data, compute_daily_returns


if __name__ == "__main__":
    # Define date range
    start_date = '2015-10-02'
    end_date = '2017-10-17'
    # Read data
    dates = pd.date_range(start_date, end_date)
    symbols = ['SPY', 'XOM', 'ALRM']
    df = get_data(symbols, dates)
    plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    #plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")

    # Plot both histogram on the same chart
    #daily_returns['SPY'].hist(bins=20, label="SPY")
    #daily_returns['XOM'].hist(bins=20, label="XOM")
    #plt.show()

    """
    # Get mean and standard deviation
    mean = daily_returns['SPY'].mean()
    print("Mean=", mean)
    std = daily_returns['SPY'].std()
    print("st.dev=",std)

    plt.axvline(mean, color='w', linestyle='dashed', linewidth=2)
    plt.axvline(std, color='r', linestyle='dashed', linewidth=2)
    plt.axvline(-std, color='r', linestyle='dashed', linewidth=2)
    plt.show()
    
    # Compute kurtosis
    print(daily_returns.kurtosis())
    """

    # Scatterplot SPY vs XOM
    daily_returns.plot(kind='scatter', x='SPY', y='XOM')
    beta_XOM, alpha_XOM = np.polyfit(daily_returns['SPY'], daily_returns['XOM'], 1)
    print("beta_XOM=", beta_XOM)
    print("alpha_XOM=", alpha_XOM)
    plt.plot(daily_returns['SPY'], beta_XOM*daily_returns['SPY'] + alpha_XOM, '-', color='r')
    plt.show()

    # Scatterplot SPY vs ALRM
    daily_returns.plot(kind='scatter', x='SPY', y='ALRM')
    beta_ALRM, alpha_ALRM = np.polyfit(daily_returns['SPY'], daily_returns['ALRM'], 1)
    print("beta_ALRM=", beta_ALRM)
    print("alpha_ALRM=", alpha_ALRM)
    plt.plot(daily_returns['SPY'], beta_ALRM*daily_returns['SPY'] + alpha_ALRM, '-', color='r')
    plt.show()

    # Calculate correlation coefficient
    print(daily_returns.corr(method='pearson'))

