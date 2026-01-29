#This file is for holding the tickers for the stocks we want to use for our app

#The stock tickers for the stock we are going to use
stock_tickers = ['MSFT', 'AAPL', 'META', 'INTC', 'NVDA']

#loop through each stock convert it into the format needed for the yfinance package
def stocks():
    stocks = ''
    for stock in stock_tickers:
        stocks += stock + ' '
    return stocks