import ccxt
import pandas as pd

def get_data(symbol, timeframe, limit) -> pd.DataFrame:
    exchange = ccxt.binance()
    raw_data = exchange.fetch_open_interest_history(symbol, timeframe, limit=limit)
    df = pd.DataFrame(raw_data)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df = df[['timestamp', 'openInterestAmount']]
    df.columns = ['Date', 'Open_Interest']
    df.set_index('Date', inplace=True)
    df['Open_Interest'] = pd.to_numeric(df['Open_Interest'])
    return df
