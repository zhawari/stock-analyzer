import config as cfg
import fetchdata
import classes

import requests
import pandas as pd
import numpy as np
from fbprophet import Prophet
import matplotlib.pyplot as plt

def basic_analzye(): #Uses Facebook Prophet to predict trends
    #help(Prophet)
    #help(Prophet.fit)
    df = pd.read_csv('%s.csv' % cfg.symbol)

    #if cfg.crypto != True:
    df['y'] = np.log(df["adjusted_close"])
    #else:
        #df['y'] = np.log(df["closeUSD"])
        # If crypto use "closeUSD"
    df.head()

    m = Prophet()
    m.fit(df);

    future = m.make_future_dataframe(periods=365)
    future.tail()

    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    m.plot_components(forecast);
    plt.show()

def advanced_analyze():

    df = pd.read_csv('%s.csv' % cfg.symbol)

    period = input("How many days do you want to predict? Leave blank for 365 days. 'A' for a period equal to all history.\n")
    if period is "":
        period = 365
    if period is 'A':
        period = len(df["ds"])
    print("Prediction period is " + str(period) + " days.\n")

    comp = input("Show components? (Y/N) Default is no.\n -> ")
    if comp is "Y":
        comp = True
    else:
        comp = False


    index = input("What do you want to track? Adjusted close is default. Options are: 'V' for volume; 'D' for dividend; 'L' for low; and 'H' for high.\n -> ")
    if index is 'V':
        df['y'] = np.log(df["volume"])
    elif index is 'D':
        df['y'] = np.log(df["dividend"])
    elif index is 'L':
        df['y'] = np.log(df["low"])
    elif index is 'H':
        df['y'] = np.log(df["high"])
    else:
        #if cfg.crypto != True:
        df['y'] = np.log(df["adjusted_close"])
        #else:
            #df['y'] = np.log(df["closeUSD"])
            # If crypto use "closeUSD"

    change = input("Do you want change the changepoint_prior_scale? Increase to make the prediction more flexible. Default is 1.\n -> ")
    if change is '':
        change = 1

    df.head()

    m = Prophet(changepoint_prior_scale=change)
    m.fit(df);

    future = m.make_future_dataframe(periods = period)
    future.tail()

    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

    if comp is True:
        m.plot_components(forecast);
    else:
        m.plot(forecast);

    plt.show()

def main():
    advanced = input("Advanced analysis? (Y/N)\n -> ")

    if advanced is 'Y':
        adv = advanced_analyze()
    else:
        ana = basic_analzye()


main()
