import pandas as pd
from fear_and_greed import FearAndGreedIndex

def get_data() -> pd.DataFrame:
    df_fng = pd.DataFrame(FearAndGreedIndex().get_last_n_days(5000))
    df_fng = df_fng.sort_values(by='timestamp', ascending=True)
    df_fng['timestamp'] = pd.to_datetime(df_fng['timestamp'].astype(int), unit='s')
    df_fng['timestamp'] = df_fng['timestamp'].dt.strftime('%m/%d/%Y')
    df_fng = df_fng[['timestamp', 'value']]
    df_fng.columns = ['Date', 'Value']
    return df_fng
