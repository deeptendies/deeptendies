import datetime

import yfinance as yf
import pandas as pd
import json
from datetime import date
from pandas_datareader import data as pdr
pd.options.plotting.backend = "plotly"

"""Main module."""
class DataFrame:
    def __init__(self, *args, **kwargs):
        yf.pdr_override()

    @staticmethod
    def from_yf(ticker, start=date.today() - datetime.timedelta(days=10 * 365), end=date.today()):
        """returns a pandas dataframe containing the last 10 years of data"""
        df = pdr.get_data_yahoo(ticker, start=start, end=end)
        df.columns = [x.lower().replace(" ", "_") for x in df.columns]
        return df

    @staticmethod
    def from_yf_info(ticker):
        yft = yf.Ticker(ticker)
        df = pd.DataFrame([yft.info], columns=yft.info.keys()).T
        df.columns = ['value']
        return df
