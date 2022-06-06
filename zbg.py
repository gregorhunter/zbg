#!/usr/bin/env python3

# dependencies

import pandas as pd
import pandas_datareader.data as web
from pandas.tseries.offsets import BDay
from pandas.tseries.offsets import DateOffset
import matplotlib.pyplot as plt
import yfinance as yf

import sys
import datetime as dt
from datetime import timedelta
from datetime import date

# formatting options

pd.set_option('display.float_format', '{:.2f}'.format)

# inputs

ticker = sys.argv[1]
try:
    func = sys.argv[2].upper()
except IndexError:
    func = "Q"
try:
    flag = sys.argv[3].upper()
except IndexError:
    flag = "D"

# time handling
    # returns start, finish

    # TODO holiday handling
    # TODO time zone handling

def time(flag):
    # selects dates for API call. Currently consists of today, one 
    # year ago, and the start of the year

    def businessDayConverter(date):
        # converts a date to the previous business day
        return pd.offsets.BDay().rollback(date) 

    today = dt.datetime.today()
    oneYearAgo = today - DateOffset(months=12)
    lastYearEnd = date(dt.datetime.today().year - 1, 12, 31)

    today = businessDayConverter(today)
    oneYearAgo =  businessDayConverter(oneYearAgo)
    lastYearEnd = businessDayConverter(lastYearEnd)

    # debugger
    # print(f"Today: {today}\nOne year ago: {oneYearAgo}\nLast year end: {lastYearEnd}\n")
    
    # set period to year-to-date
    if flag == "YTD":
        return lastYearEnd, today
    else:
        return oneYearAgo, today

def api_call(ticker, start, end):
    # call to pandas web datareader. Returns dataframe
    return web.DataReader(ticker, 'yahoo', start=start, end=end)

def hcp(stockData, flag=["D"]):
    # Replicates HCP function call. Displays historical price changes.

    # TODO allow for flags for different periods (1Y by default, YTD etc)
    
    outputData = stockData.iloc[::-1].copy()

    # if flag == "M":
    #     stockData.index = stockData.index(pd.date_range(stockData.index[0], stockData.index[-1], freq="M"))
    #     print(stockData)

    # calculates price change
    outputData['Daily Change'] = outputData['Close'].diff(-1)
    # calculates percentage change
    outputData['Daily Percent Change (%)'] = outputData['Close'].pct_change(-1) * 100
    # calculates cumulative percentage change
    outputData['Cumulative Percent Change (%)'] = ((outputData['Close']/outputData['Close'].iloc[-1])) * 100
    print(outputData.loc[:,('Close','Daily Change','Daily Percent Change (%)', 'Cumulative Percent Change (%)')][:-1])

def gp(stockData):
    # displays a graphic of the stock price and volume

    stock = stockData['Close']
    volume = stockData['Volume']
    companyInfo = yf.Ticker(ticker).info
    companyName = companyInfo['shortName']
    stockCurrency = companyInfo['currency']
    
    fig, (ax1, ax2) = plt.subplots(2, 1)

    stockData['Close'].plot(y='Close', ax=ax1)
    ax1.set_title(companyName)
    ax1.yaxis.set_label_text(f'Price ({stockCurrency})')
    ax1.set_xticklabels([])

    stockData['Volume'].plot(y='Volume', ax=ax2)
    ax2.xaxis.set_label_text('Date')
    ax2.yaxis.set_label_text('Volume')    

    ax1.grid()
    ax2.grid()
    plt.show()

# TODO fully implement Q

def q(stockData):
    # TODO decide what you want output to look like
    print(stockData.iloc[0])

# TODO implement FRED

# TODO implement bonds

# output to excel. currently not used

def outputExcel(stockData):
    stockData.to_excel(r'output.xlsx')

# function selection

def runZBG(start, end, ticker, func, flag=""): stockData = api_call(ticker, start, end)
    if func == "GP": 
        gp(stockData)
    elif func == "HCP":
        hcp(stockData, flag)
    else:
        q(stockData)

start, end = time(flag)
runZBG(start, end, ticker, func)
