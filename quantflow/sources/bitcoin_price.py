import yfinance as yf
import pandas as pd

def get_data() -> pd.DataFrame:
    btc = yf.Ticker('BTC-USD')
    hist = btc.history(period='max')
    hist = hist[['Open', 'High', 'Low', 'Close']]
    hist = hist.reset_index(inplace=False)
    hist['Date'] = pd.to_datetime(hist['Date'])
    hist['Date'] = hist['Date'].dt.strftime('%m/%d/%Y')
    return hist
