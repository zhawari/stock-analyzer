import config as cfg
import csv

with open('%s.csv' % cfg.symbol, 'r') as stock_file:
    reader = csv.reader(stock_file)
    stocks = list(reader)

class Exchange:
    def __init__(self, datestamp, open_price, high,
        low, close_price, adjusted_close,
        volume, dividend, split):
        self.ds = datestamp
        self.o = open_price
        self.h = high
        self.l = low
        self.c = close_price
        self.a = adjusted_close
        self.v = volume
        self.d = dividend
        self.s = split
try:
    st = Exchange([item[1] for item in stocks], [item[2] for item in stocks],
            [item[3] for item in stocks], [item[4] for item in stocks],
            [item[5] for item in stocks], [item[6] for item in stocks],
            [item[7] for item in stocks], [item[8] for item in stocks],
            [item[9] for item in stocks])
except IndexError:
    print("IndexError in classes.py Exchange. Check whether a cfg.sybmol.csv file was downloaded and accessed.")

# Get sector data in JSON
import requests
import json
sec_json = requests.get('https://www.alphavantage.co/query?function=SECTOR&apikey=&apikey=471AB4KLSLJV6Q4A').json()
rank = ["Rank A: Real-Time Performance", "Rank B: 1 Day Performance", "Rank C: 5 Day Performance", "Rank D: 1 Month Performance", "Rank E: 3 Month Performance", "Rank F: Year-to-Date (YTD) Performance", "Rank G: 1 Year Performance", "Rank H: 3 Year Performance", "Rank I: 5 Year Performance", "Rank J: 10 Year Performance"]

class Sector:
    def __init__(self, real_time, one_day, five_day, one_month, three_month, YTD, one_year, three_year, five_year, ten_year):
        self.rt = real_time
        self.od = one_day
        self.fd = five_day
        self.om = one_month
        self.tm = three_month
        self.ytd = YTD
        self.oy = one_year
        self.ty = three_year
        self.fy = five_year
        self.teny = ten_year

ind = Sector(sec_json[rank[0]]["Industrials"], sec_json[rank[1]]["Industrials"],
                        sec_json[rank[2]]["Industrials"], sec_json[rank[3]]["Industrials"],
                        sec_json[rank[4]]["Industrials"], sec_json[rank[4]]["Industrials"],
                        sec_json[rank[6]]["Industrials"], sec_json[rank[7]]["Industrials"],
                        sec_json[rank[8]]["Industrials"], sec_json[rank[9]]["Industrials"],
                        )

fin = Sector(sec_json[rank[0]]["Financials"], sec_json[rank[1]]["Financials"],
                        sec_json[rank[2]]["Financials"], sec_json[rank[3]]["Financials"],
                        sec_json[rank[4]]["Financials"], sec_json[rank[4]]["Financials"],
                        sec_json[rank[6]]["Financials"], sec_json[rank[7]]["Financials"],
                        sec_json[rank[8]]["Financials"], sec_json[rank[9]]["Financials"],
                        )

tel = Sector(sec_json[rank[0]]["Telecommunication Services"], sec_json[rank[1]]["Telecommunication Services"],
                        sec_json[rank[2]]["Telecommunication Services"], sec_json[rank[3]]["Telecommunication Services"],
                        sec_json[rank[4]]["Telecommunication Services"], sec_json[rank[4]]["Telecommunication Services"],
                        sec_json[rank[6]]["Telecommunication Services"], sec_json[rank[7]]["Telecommunication Services"],
                        sec_json[rank[8]]["Telecommunication Services"], sec_json[rank[9]]["Telecommunication Services"],
                        )

disc = Sector(sec_json[rank[0]]["Consumer Discretionary"], sec_json[rank[1]]["Consumer Discretionary"],
                        sec_json[rank[2]]["Consumer Discretionary"], sec_json[rank[3]]["Consumer Discretionary"],
                        sec_json[rank[4]]["Consumer Discretionary"], sec_json[rank[4]]["Consumer Discretionary"],
                        sec_json[rank[6]]["Consumer Discretionary"], sec_json[rank[7]]["Consumer Discretionary"],
                        sec_json[rank[8]]["Consumer Discretionary"], sec_json[rank[9]]["Consumer Discretionary"],
                        )

tech = Sector(sec_json[rank[0]]["Information Technology"], sec_json[rank[1]]["Information Technology"],
                        sec_json[rank[2]]["Information Technology"], sec_json[rank[3]]["Information Technology"],
                        sec_json[rank[4]]["Information Technology"], sec_json[rank[4]]["Information Technology"],
                        sec_json[rank[6]]["Information Technology"], sec_json[rank[7]]["Information Technology"],
                        sec_json[rank[8]]["Information Technology"], sec_json[rank[9]]["Information Technology"],
                        )

util = Sector(sec_json[rank[0]]["Utilities"], sec_json[rank[1]]["Utilities"],
                        sec_json[rank[2]]["Utilities"], sec_json[rank[3]]["Utilities"],
                        sec_json[rank[4]]["Utilities"], sec_json[rank[4]]["Utilities"],
                        sec_json[rank[6]]["Utilities"], sec_json[rank[7]]["Utilities"],
                        sec_json[rank[8]]["Utilities"], sec_json[rank[9]]["Utilities"],
                        )

care = Sector(sec_json[rank[0]]["Health Care"], sec_json[rank[1]]["Health Care"],
                        sec_json[rank[2]]["Health Care"], sec_json[rank[3]]["Health Care"],
                        sec_json[rank[4]]["Health Care"], sec_json[rank[4]]["Health Care"],
                        sec_json[rank[6]]["Health Care"], sec_json[rank[7]]["Health Care"],
                        sec_json[rank[8]]["Health Care"], sec_json[rank[9]]["Health Care"],
                        )

real = Sector(sec_json[rank[0]]["Real Estate"], sec_json[rank[1]]["Real Estate"],
                        sec_json[rank[2]]["Real Estate"], sec_json[rank[3]]["Real Estate"],
                        sec_json[rank[4]]["Real Estate"], sec_json[rank[4]]["Real Estate"],
                        0,0,0,0,
                        )

stap = Sector(sec_json[rank[0]]["Consumer Staples"], sec_json[rank[1]]["Consumer Staples"],
                        sec_json[rank[2]]["Consumer Staples"], sec_json[rank[3]]["Consumer Staples"],
                        sec_json[rank[4]]["Consumer Staples"], sec_json[rank[4]]["Consumer Staples"],
                        sec_json[rank[6]]["Consumer Staples"], sec_json[rank[7]]["Consumer Staples"],
                        sec_json[rank[8]]["Consumer Staples"], sec_json[rank[9]]["Consumer Staples"],
                        )

en = Sector(sec_json[rank[0]]["Energy"], sec_json[rank[1]]["Energy"],
                        sec_json[rank[2]]["Energy"], sec_json[rank[3]]["Energy"],
                        sec_json[rank[4]]["Energy"], sec_json[rank[4]]["Energy"],
                        sec_json[rank[6]]["Energy"], sec_json[rank[7]]["Energy"],
                        sec_json[rank[8]]["Energy"], sec_json[rank[9]]["Energy"],
                        )

mat = Sector(sec_json[rank[0]]["Materials"], sec_json[rank[1]]["Materials"],
                        sec_json[rank[2]]["Materials"], sec_json[rank[3]]["Materials"],
                        sec_json[rank[4]]["Materials"], sec_json[rank[4]]["Materials"],
                        sec_json[rank[6]]["Materials"], sec_json[rank[7]]["Materials"],
                        sec_json[rank[8]]["Materials"], sec_json[rank[9]]["Materials"],
                        )
