import csv
import requests
import pandas as pd
import config as cfg
import os
import json
import pickle
#print("Your file is in" + os.getcwd())

'''
fetchdata = fetch.main()
Make sure to define symbol in config.py
'''
# See https://www.alphavantage.co/documentation/ for more info
url_base = "https://www.alphavantage.co/query?"
api_key = "&apikey=471AB4KLSLJV6Q4A"
make_csv = "&datatype=csv"
output = "&outputsize=full" # Full gets all stock data in database; compact gets last 100 entries

# Crypto functions have been disabled
def getcryptodata():
    url_base = "https://www.alphavantage.co/query?"
    url_function = "function=DIGITAL_CURRENCY_DAILY"
    market = "&market=CNY" #DIGITAL_CURRENCY_DAILY only
    # See https://www.alphavantage.co/documentation/ for more info
    api_key = "&apikey=471AB4KLSLJV6Q4A"
    make_csv = "&datatype=csv"

    csv_url = url_base + url_function + "&symbol=" \
    + cfg.symbol + market + api_key + make_csv
    #print(csv_url)

    r = requests.get(csv_url, allow_redirects=True)
    open(cfg.csv_file, 'wb').write(r.content)
    df = pd.read_csv(cfg.csv_file)
    df.columns = ('ds', 'openCNY', 'highCNY', 'lowCNY', 'closeCNY', 'openUSD', 'highUSD', 'lowUSD', 'closeUSD', 'volume', 'market_capUSD')
    df.to_csv(cfg.csv_file, index=False)

def getmindata():
    url_function = "function=TIME_SERIES_INTRADAY"
    interval = "&interval="
    interval_dur = cfg.interval

    csv_url = url_base + url_function + "&symbol=" \
    + cfg.symbol + interval + api_key + make_csv
    print(csv_url)

    r = requests.get(csv_url, allow_redirects=True)
    open('%s.csv' % cfg.symbol, 'wb').write(r.content)

    df = pd.read_csv('min_%s.csv' % cfg.symbol)
    df.columns = ('ds','open','high','low','close','volume')
    df.to_csv('%s.csv' % cfg.symbol)

def getstockdata():
    url_function = "function=TIME_SERIES_DAILY_ADJUSTED"
    csv_url = url_base + url_function + "&symbol=" \
    + cfg.symbol + output + api_key + make_csv
    #print(csv_url)

    r = requests.get(csv_url, allow_redirects=True)
    open('%s.csv' % cfg.symbol, 'wb').write(r.content)

    df = pd.read_csv('%s.csv' % cfg.symbol)

    df.columns = ('ds','open','high','low','close','adjusted_close','volume','dividend_amount','split_coefficient')
    df.to_csv('%s.csv' % cfg.symbol)

def getaverage():
    url_function = "function=SMA"
    url = url_base + url_function + "&symbol=" \
    + "T" + "&interval=" + cfg.interval + "&time_period=" + cfg.period + "&series_type=close" + api_key
    print(url)

    #demo url: (https://www.alphavantage.co/query?)(function=SMA)(&symbol=MSFT)(&interval=15min)(&time_period=10)(&series_type=close)(&apikey=demo)

    avg_request = requests.get(url, allow_redirects=True)
    avg_json = avg_request.json()
    #print(avg_json)
    date = list(avg_json['Technical Analysis: SMA'].keys())
    print(date)

    num = len(date)
    sma = []
    print(num)
    for i in range(num):
        s = date[i]
    res = pickle.dumps(sma)
    print(res)

'''
    class Average:
        def __init__(self, date, moving_average):
            self.d = date
            self.mov = moving_average

    #sma = Average(avg_json['Technical Analysis: SMA'].keys(),avg_json[])
    #print (Average.d)
'''
def main():
    #if cfg.symbol == "":
    #    cfg.symbol = "T"
    #if cfg.crypto == True:
        #getcrypto = getcryptodata()
        #print('Here is your crypto currency data for ' + cfg.symbol + '.')
    #else:
    getstock = getstockdata()
    print('Here is your stock data for ' + cfg.symbol + '.')

getaverage()
