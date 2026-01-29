#Benjamin Odell
#Mini Project 1

import yfinance as yf
import pprint
import stock_tickers
import numpy as np
import matplotlib.pyplot as plt
from os import makedirs, path

#Get the tickers for my chosen stocks
stocks = yf.Tickers(stock_tickers.stocks())

#create a dict for holding the closing data
closing = {}

#loop through each stock in tickers gather closing data
for ticker in stocks.tickers:
    data = yf.Ticker(ticker).history(period="10d")['Close']
    closing[ticker] = np.array(data)

#checks if there is a plots dir if not create one
if not path.isdir('plots'):
    makedirs('plots')

#loop through each ticker and output image with matplot lib
for stock in closing:
    plt.plot(closing[stock])
    plt.savefig(path.join(path.dirname(__file__), 'plots', stock + '.png'))
    plt.close()
#prints out data
pprint.pprint(closing)