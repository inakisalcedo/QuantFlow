import pandas as pd
from .sources import bitcoin_price
from .sources import buffet_indicator
from .sources import dollar_strength
from .sources import fear_greed
from .sources import nfci_index
from .sources import open_interest_data

def btc_price() -> pd.DataFrame:
    return bitcoin_price.get_data()

def buffet() -> pd.DataFrame:
    return buffet_indicator.get_data()

def dxy(start='2017-1-1') -> pd.DataFrame:
    return dollar_strength.get_data(start)

def fng() -> pd.DataFrame:
    return fear_greed.get_data()

def nfci() -> pd.DataFrame:
    return nfci_index.get_data()

def open_interest(symbol='BTC/USDT:USDT', timeframe='1d', limit=100) -> pd.DataFrame:
    return open_interest_data.get_data(symbol, timeframe, limit)
