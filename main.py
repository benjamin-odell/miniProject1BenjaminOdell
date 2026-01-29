#Benjamin Odell
#Mini Project 1

import yfinance as yf
import pprint
import stock_tickers
import numpy as np
import matplotlib.pyplot as plt

#Get the tickers for my chosen stocks
stocks = yf.Tickers(stock_tickers.stocks())

#create a dict for holding the closing data
closing = {}

#loop through each stock in tickers gather closing data
for ticker in stocks.tickers:
    data = yf.Ticker(ticker).history(period="10d")['Close']
    closing[ticker] = []
    for d in data:
        closing[ticker].append(d)

#prints out data
pprint.pprint(closing)