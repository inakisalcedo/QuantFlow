import yfinance as yf
import pandas_datareader.data as web
import pandas as pd
import datetime

def get_data() -> pd.DataFrame:
    start = "2000-01-01"
    w5000 = yf.download("^W5000", start=start, auto_adjust=True)
    if w5000.empty:
        w5000 = yf.download("VTI", start=start, auto_adjust=True)
    if isinstance(w5000.columns, pd.MultiIndex):
        close_prices = w5000['Close'].iloc[:, 0]
    else:
        close_prices = w5000['Close']
    market_cap = close_prices.to_frame(name='MarketCap')
    try:
        gdp = web.get_data_fred('GDP', start=start)
        gdp.index.name = 'Date'
    except Exception as e:
        print(f"Error al conectar con FRED: {e}")
        return pd.DataFrame()
    df = market_cap.join(gdp, how='left')
    df['GDP'] = df['GDP'].ffill()
    df['Buffett_Indicator'] = (df['MarketCap'] / df['GDP']) * 100
    return df.dropna()
