# import os
import yfinance as yf
import pandas as pd
import requests as rq

DATASET = 'e:/Python Projects/datasets/stocks'
PORTFOLIO = ['NIO', 'SE', 'PLTR', 'TSLA', 'SQ', 'ROKU', 'MELI', 'NVDA', 'AAPL', 'FB', 'TDOC', 'SBUX', 'BIDU', 'NVAX', 'GLBE', 'WMT']


# GET NASDAQ TICKERS

#Read data from Wiki
nasdaq_data = rq.get('https://en.wikipedia.org/wiki/NASDAQ-100#Changes_in_2020').text

#Put data into Pandas to easily create a list of tickers to loop through
nasdaq_df = pd.read_html(nasdaq_data)

#Finds the Wiki table with tickers and stores them in Pandas Data Frame
nasdaq_df = nasdaq_df[3]

#Creates a list of tickers from Data Frame to loop through
nasdaq_tickers = list(nasdaq_df['Ticker'])


# GET SP500 TICKERS

#Read data from Wiki
sp500_data = rq.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies').text

#Put data into Pandas to easily create a list of tickers to loop through
sp500_df = pd.read_html(sp500_data)

#Finds the Wiki table with tickers and stores them in Pandas Data Frame
sp500_df = sp500_df[0]

#Creates a list of tickers from Data Frame to loop through
sp500_tickers = list(sp500_df['Symbol'])


# Loop through all tickers and save OHLCV data into csv
for ticker in nasdaq_tickers:
    data = yf.download(ticker, start="2021-01-01")
    data.to_csv(f'{DATASET}/{ticker}.csv')

for ticker in sp500_tickers:
    data = yf.download(ticker, start="2021-01-01")
    data.to_csv(f'{DATASET}/{ticker}.csv')

for ticker in PORTFOLIO:
    data = yf.download(ticker, start="2021-01-01")
    data.to_csv(f'{DATASET}/{ticker}.csv')


# with open('symbols.csv') as f:
#     lines = f.read().splitlines()
#     for symbol in lines:
#         print(symbol)
#         data = yf.download(symbol, start="2021-05-01", end="2020-08-22")
#         data.to_csv("datasets/{}.csv".format(symbol))