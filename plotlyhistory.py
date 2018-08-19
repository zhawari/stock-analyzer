# plotly.tools.set_credentials_file(username='zacharyth', api_key='Lwv49icVWWdcvPgMfBH8')
# Use plotly.offline.plot() to create and standalone HTML that is saved locally and opened inside your web browser.
import config as cfg
import classes
import fetchdata

import plotly.plotly as py
import plotly
import plotly.graph_objs as go
from plotly import tools

import matplotlib

import pandas as pd
import numpy as np

def plot():

    data = [go.Scatter(
          x = classes.st.ds[0:int(cfg.period)],
          y = classes.st.a[0:int(cfg.period)]
          )]

    plotly.offline.plot(data)

def sector():
    trace1 = go.Bar(
        x=['Real Time Performance', 'Five Day', 'One Month' 'YTD', 'Five Year'],
        y=[classes.ind.rt, classes.ind.fd, classes.ind.om, classes.ind.ytd, classes.ind.fy],
        name='Industrials'
    )
    trace2 = go.Bar(
        x=['Real Time Performance', 'Five Day', 'One Month' 'YTD', 'Five Year'],
        y=[classes.fin.rt, classes.fin.fd, classes.fin.om, classes.fin.ytd, classes.fin.fy],
        name='Financials'
    )
    trace3 = go.Bar(
        x=['Real Time Performance', 'Five Day', 'One Month' 'YTD', 'Five Year'],
        y=[classes.tel.rt, classes.tel.fd, classes.tel.om, classes.tel.ytd, classes.tel.fy],
        name='Telecommunication'
    )
    trace4 = go.Bar(
        x=['Real Time Performance', 'Five Day', 'One Month' 'YTD', 'Five Year'],
        y=[classes.disc.rt, classes.disc.fd, classes.disc.om, classes.disc.ytd, classes.disc.fy],
        name='Consumer Discretionary'
    )
    trace5 = go.Bar(
        x=['Real Time Performance', 'Five Day', 'One Month' 'YTD', 'Five Year'],
        y=[classes.tech.rt, classes.tech.fd, classes.tech.om, classes.tech.ytd, classes.tech.fy],
        name='Technology'
    )
    trace6 = go.Bar(
        x=['Real Time Performance', 'Five Day', 'One Month' 'YTD', 'Five Year'],
        y=[classes.util.rt, classes.util.fd, classes.util.om, classes.util.ytd, classes.util.fy],
        name='Utilities'
    )
    trace7 = go.Bar(
        x=['Real Time Performance', 'Five Day', 'One Month' 'YTD', 'Five Year'],
        y=[classes.care.rt, classes.care.fd, classes.care.om, classes.care.ytd, classes.care.fy],
        name='Health Care'
    )
    trace8 = go.Bar(
        x=['Real Time Performance', 'Five Day', 'One Month' 'YTD', 'Five Year'],
        y=[classes.stap.rt, classes.stap.fd, classes.stap.om, classes.stap.ytd, classes.stap.fy],
        name='Consumer Staples'
    )
    trace9 = go.Bar(
        x=['Real Time Performance', 'Five Day', 'One Month' 'YTD', 'Five Year'],
        y=[classes.en.rt, classes.en.fd, classes.en.om, classes.en.ytd, classes.en.fy],
        name='Energy'
    )
    trace10 = go.Bar(
        x=['Real Time Performance', 'Five Day', 'One Month' 'YTD', 'Five Year'],
        y=[classes.mat.rt, classes.mat.fd, classes.mat.om, classes.mat.ytd, classes.mat.fy],
        name='Materials'
    )

    data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10]
    layout = go.Layout(
    barmode='group'
    )
    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename='grouped-bar')

def candlestick():
    #from datetime import datetime

    #df = web.DataReader("aapl", 'yahoo')
    #df = pd.read_csv('%s.csv' % cfg.symbol)

    trace = go.Candlestick(x=classes.st.ds[0:int(cfg.period)],
                           open=classes.st.o[0:int(cfg.period)],
                           high=classes.st.h[0:int(cfg.period)],
                           low=classes.st.l[0:int(cfg.period)],
                           close=classes.st.c[0:int(cfg.period)])
    data = [trace]
    layout = {
    'title': 'Stock Data for ' + cfg.symbol,
    'yaxis': {'title': cfg.symbol + 'Stock'},
    'shapes': [{
        'x0': classes.st.ds[0], 'x1': classes.st.ds[len(classes.st.ds)-1],
        'y0': 0, 'y1': 1, 'xref': 'x', 'yref': 'paper',
        'line': {'color': 'rgb(30,30,30)', 'width': 1},
        }],
    #'annotations': [{
    #    'x': '2016-12-09', 'y': 0.05, 'xref': 'x', 'yref': 'paper',
    #    'showarrow': False, 'xanchor': 'left',
    #    'text': 'Increase Period Begins'
    #    }]
    }
    fig = dict(data=data, layout=layout)
    plotly.offline.plot(data, filename='Stock Table with Titles & Annotation')

def multiple():
    from plotly import tools

    trace1 = go.Scatter(
        x= classes.st.ds[0:int(cfg.period)],
        y= classes.st.a[0:int(cfg.period)],
        name='Adjusted Close'
    )
    trace2 = go.Bar(
        x= classes.st.ds[0:int(cfg.period)],
        y= classes.st.v[0:int(cfg.period)],
        name='Volume'
    )
    trace3 = go.Bar(
        x= classes.st.ds[0:int(cfg.period)],
        y= classes.st.d[0:int(cfg.period)],
        name='Dividends'
    )
    fig = tools.make_subplots(rows=3, cols=1)

    fig.append_trace(trace1, 1, 1)
    fig.append_trace(trace2, 2, 1)
    fig.append_trace(trace3, 3, 1)

    fig['layout']['yaxis1'].update(title='Adjusted Close in Dollars')
    fig['layout']['yaxis2'].update(title='Number of Stocks Traded')
    fig['layout']['yaxis3'].update(title='Dividends Dispersed in Dollars')

    fig['layout'].update(title='Stock data for %s' % cfg.symbol)
    #data = [trace1, trace2, trace3]
    #fig = tools.make_subplots()
    #layout = go.Layout(
    #    yaxis=dict(
    #        domain=[0, 0.33]
    #    ),
    #    legend=dict(
    #        traceorder='reversed'
    #    ),
    #    yaxis2=dict(
    #        domain=[0.33, 0.66]
    #    ),
    #    yaxis3=dict(
    #        domain=[0.66, 1]
    #    )
    #)
    #fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename='stacked-subplots-shared-x-axis')

def interval():
    cfg.interval = input("What do you want the interval of the data? Options: 1min, 5min, 15min, 30min, 60min\n -> ")
    fetch = fetchdata.getmindata()

    df = pd.read_csv('min_%s.csv' % cfg.symbol)

    data = [go.Scatter(
          x = df['close'][0:99],
          y = df['ds'][0:99]
          )]

    plotly.offline.plot(data)

def main():
    cfg.period = input("How many days do want to chart? Leave blank for all data.\n -> ")
    if cfg.period is "":
        cfg.period = len(classes.st.ds)
    print("Chart will display " + str(cfg.period) + " days.")

    plot_type = input("What kind of plot do you want? Defalut is line. To change: C for candlestick, S for sector-by-sector comparison, M for plot with Adjusted Close, Volume, and Dividends. Default is Line.\n -> ")
    if plot_type is 'C':
        candle = candlestick()
        quit()
    elif plot_type is 'M':
        plotm = multiple()
        quit()
    elif plot_type is 'S':
        sec = sector()
        quit()
    else:
        plotit = plot()
        quit()


main()
