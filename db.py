from config import config, tickers
import pandas as pd
import sqlite3
import yfinance


def get_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected. Version: {sqlite3.version}")
    except sqlite3.Error as e:
        print(e)
    return conn


if __name__ == '__main__':
    conn = get_connection(config.daily_db)
    if conn is not None:
        data = yfinance.download(" ".join(tickers.tickers['AEX']), actions=True, group_by="tickers")
        for ticker in tickers.tickers['AEX']:
            subset = data[ticker]
            subset.columns = subset.columns.str.lower().str.replace(" ", "_")
            start = subset.iloc[:, 0].first_valid_index()
            end = subset.iloc[:, 0].last_valid_index()
            subset = subset.loc[start:end, :]
            subset.to_sql(ticker, conn, if_exists='append')
