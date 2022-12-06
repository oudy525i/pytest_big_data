import sys
import datetime
from yahoofinancials import YahooFinancials
import json
from pandas.io.json import json_normalize
import pandas as pd
import urllib
import requests
import unittest

def get_stock_historical_data(ticker):
        #stock_historical_data_array = []
        base_url = "https://query1.finance.yahoo.com/v11/finance/quoteSummary/"
        #tickerStock = YahooFinancials(quote)
        #json1 = tickerStock.get_historical_price_data('2015-01-15', '2022-11-20', "weekly")
        response = requests.get(base_url+ticker)
        status_code = response.status_code
    
        assert response.status_code == 200, print("Got wrong status code, expected is: {}, actual is  {}".format("200", response.status_code))
        return status_code

print (get_stock_historical_data (ticker="AAPL"))