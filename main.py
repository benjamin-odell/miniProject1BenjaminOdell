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
    dates = np.array(data.axes[0].array)

    #holds dates for the plot
    axis = []

    #loop through dates and format each date for mouth and day
    for date in dates:
        axis.append(date.strftime('%m/%d'))

    #stores data and date into the closing dict
    closing[ticker] = [axis, data]

#holds names for folder to hold plots
folder_name = 'charts'
#checks if there is a plots dir if not create one
if not path.isdir(folder_name):
    makedirs(folder_name)

#loop through each ticker and output image with matplot lib
for stock in closing:
    #plot figure
    plt.plot(closing[stock][0], closing[stock][1], label=stock)
    #add figures labels
    plt.title(f"{stock}'s Closing Price($)")
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    #save figure
    plt.savefig(path.join(path.dirname(__file__), folder_name, stock + '.png'))
    plt.close()