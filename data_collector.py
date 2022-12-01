# import a bunch of libraries
import sys
import datetime
from yahoofinancials import YahooFinancials
import json
from pandas.io.json import json_normalize
import pandas as pd


def stockPicker(ticker, freq):
    #Get price form yahoo API
    tickerStock = YahooFinancials(ticker)
    tickerPrice = tickerStock.get_historical_price_data('2015-01-15', '2022-11-20', freq)
        
    ticker_df = pd.DataFrame.from_dict(tickerPrice[ticker]["prices"])

    ticker_df.to_csv('out.zip', index=False,compression='infer')  

    return (ticker_df.head(5))
print(stockPicker("AAPL", "weekly"))