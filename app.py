# import a bunch of libraries
import sys
import datetime
from yahoofinancials import YahooFinancials
import json
from pandas.io.json import json_normalize
import pandas as pd
#import datatest as dt
import pytest
import unittest

def stockPicker(ticker, freq):
   
   #Get price form yahoo API
   tickerStock = YahooFinancials(ticker)
   tickerPrice = tickerStock.get_historical_price_data('2015-01-15', '2022-11-20', freq)
    
   ticker_df = pd.DataFrame.from_dict(tickerPrice[ticker]["prices"])

   df_expected = pd.DataFrame('date', 'high', 'low', 'open', 'close', 'volume', 'adjclose', 'formatted_date')

   assert ticker_df.columns.equals(df_expected)

   c = []
   for col in ticker_df.columns:
        c.append(col)
        
   return (ticker_df.head(5))
   #return c


#def ticker_test():
    #assert stockPicker().is_upper()

#if __name__ == "__main__":
    #ticker = input("please enter a stock ticker: ")
    #freq = input("please enter frequence, either monthly or weekly: ")
print(stockPicker("AAPL", "weekly"))
#print(ticker_df.columns)
