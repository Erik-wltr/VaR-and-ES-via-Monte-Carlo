import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import pandas as pd
import yfinance as yf
from scipy.stats import norm

#sets up start and end dates
years = 15
endDate = dt.datetime.now()
startDate= endDate - dt.timedelta(days = 365*years)

#tickers 
tickers = ['SPY', 'BND', 'GLD', 'QQQ', 'VWO']

#download the dailey adjusted close prices 
adj_close_df = pd.DataFrame()
for ticker in tickers: 
    data = yf.download(ticker,start = startDate,end = endDate)
    adj_close_df[ticker] = data['Close']

#calculate the dailey ln-returns
ln_returns = np.log(adj_close_df/adj_close_df.shift(1))
ln_returns = ln_return.dropna()

#define function to calculate the future returns based on the past returns
def expected_return(weights, ln_returns):
    return np.sum(ln_returns.mean()*weights)

#define a function to calculate the protfolio standart deviation
def 

def main():
    print("start")
    print(ln_returns)
    return


if __name__ == "__main__":
    main()