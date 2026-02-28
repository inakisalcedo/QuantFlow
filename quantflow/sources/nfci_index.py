import pandas_datareader.data as web
import pandas as pd
import datetime

def get_data() -> pd.DataFrame:
    start = "2000-01-01"
    end = datetime.datetime.now()
    df = web.get_data_fred('NFCI', start, end)
    df.columns = ['NFCI']
    df.index.name = 'Date'  
    return df
