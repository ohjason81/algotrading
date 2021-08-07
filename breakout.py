import pandas as pd
import yfinance as yf
import requests as rq
import btalib as bta
import os
# from tabulate import tabulate

DATASET = 'e:/Python Projects/datasets/stocks'

def is_consolidating(df, pct=2):
    recent_data = df[-15:]

    max_close = recent_data['Close'].max()
    min_close = recent_data['Close'].min()
    
    threshold = 1 - (pct / 100)
    if min_close >= (max_close * threshold):
        return True
    
    return False

def is_breaking_out(df, pct=2.5):
    if df.empty:
        pass
    else:
        last_close = df[-1:]['Close'].values[0]

    if is_consolidating(df[:-1], pct=pct):
        recent_closes = df[-16:-1]

        if last_close > recent_closes['Close'].max():
            return True
    
    return False


for filename in os.listdir(DATASET):
    df = pd.read_csv(f'{DATASET}/{filename}')
    
    if is_consolidating(df):
        print(f'{filename.split(sep=".")[0]} is consolidating')
        # print(df['Close'][-16:-1].max(), df['Close'][-1:].values[0])
    
    if is_breaking_out(df):
        print(f'{filename.split(sep=".")[0]} is breaking out')
        # print(df['Close'][-16:-1].max(), df['Close'][-1:].values[0])
    
#     for filename in ['WMT.csv']:
#         df2 = df

# print(df2)