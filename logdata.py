import yfinance as yf
import pandas as pd
import numpy as np
from statistics import mean
from datetime import datetime


def get_data(start, end, assets):
    df = pd.DataFrame()
    for stock in assets:
        df[stock] = yf.download(stock, start=start, end=end)['Adj Close']
        df[stock].to_csv(f'{stock}.csv')
    return df


def today_date():
    return datetime.today().strftime('%Y-%m-%d')


def main():
    assets = ['VPU', 'RYU', 'XLU', 'FUTY', 'ICF']
    # Date to start collecting data. Must be a valid trading date or there will be an error.
    startDate = '2013-01-02'

    for a in assets:
        df = get_data(startDate, today_date(), assets)


main()
