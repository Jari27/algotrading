import yfinance
import pandas as pd
from config import config, tickers
import sqlite3
import os

if __name__ == '__main__':

    for key in tickers.tickers.keys():
        print(f"Downloading {key}")
        downloadables = tickers.tickers[key]
        print(f"Downloading daily data: {key}")
        data = yfinance.download(" ".join(downloadables), group_by='ticker', actions=True, period="max", interval="1d")
        print(f"Storing daily data: {key}")
        # data.to_csv(f"{config.daily_data_directory}full_{key}.csv")
        for ticker in downloadables:
            data[ticker].to_csv(f'{config.daily_data_directory}{ticker}.csv')

        print(f"Downloading 5m data: {key}")
        data = yfinance.download(" ".join(downloadables), group_by='ticker', actions=True, period="60d",
                                 interval="5m")
        print(f"Storing 5m data: {key}")
        # data.to_csv(f"{config.five_m_data_directory}full_{key}.csv")
        for ticker in downloadables:
            data[ticker].to_csv(f'{config.five_m_data_directory}{ticker}.csv')

    # flow = yfinance.Ticker("FLOW.AS")
    # print(flow.history(period="60d", interval="5m"))
