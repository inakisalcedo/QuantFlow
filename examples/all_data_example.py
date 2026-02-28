import quantflow as qf

# For symbol in open interest use: 'Crypto2/Crypto1:Crypto1'
df_oi = qf.open_interest() # Or qf.open_interest(symbol: str, timeframe: str, limit: int)
df_price = qf.btc_price()
df_nfci = qf.nfci()
df_dxy = qf.dxy() # Or qf.dxy(start_date: str)
df_buffet = qf.buffet()
df_fng = qf.fng()
