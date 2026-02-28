import yfinance as yf
import pandas as pd

def get_data(start: str) -> pd.DataFrame:
    df_dxy = yf.Ticker('DX-Y.NYB').history(start=start)
    df_dxy = df_dxy[['Close']]
    df_dxy = df_dxy.reset_index(inplace=False)
    df_dxy['Date'] = pd.to_datetime(df_dxy['Date'])
    df_dxy['Date'] = df_dxy['Date'].dt.strftime('%m/%d/%Y')
    df_dxy.columns = ['Date', 'Value']
    return df_dxy
