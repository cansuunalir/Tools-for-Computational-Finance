import requests
import csv
import pandas as pd
import matplotlib.pyplot as plt
import indicators
import strategy
from strategy import MovingAverageCrossStrategy
from portfolio import MarketOnClosePortfolio
from backtest import backtest_close

###
import datetime

import pandas as pd
from pandas_datareader import data, wb
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib as mpl

# Getting Data
# r = requests.get('http://chart.finance.yahoo.com/table.csv?s=TKGBY&a=5&b=3&c=2008&d=9&e=12&f=2016&g=d&ignore=.json')
#
# print(r.text)

# aapl = data.get_data_yahoo('TKGBY',
#                                  start=datetime.datetime(2006, 10, 1),
#                                  end=datetime.datetime(2016, 10, 12))
# print(aapl)

#---------


df = pd.read_csv('data.csv') #, index_col='Date', parse_dates=True)
df['Date'] = pd.to_datetime(df.Date)
df = df.sort('Date')
df = df.set_index('Date')

print(df)
# df['Date'] = pd.to_datetime(df['Date'])
# df['Date'] = pd.to_datetime(df['Date'])
# print(df[['Open', 'Close']].head())
# dff = pandas.DataFrame(df)
# dff.plot(x='Date', y='Open')

# print(df['Open'])

# plt.plot(df['Date'], df['Close'], linestyle='-', linewidth=1)
# plt.plot(df['Date'], df['Open'], linestyle='-', linewidth=1)
# plt.legend(['Close', 'Open'], loc='upper left')
#

mac = MovingAverageCrossStrategy(df, short_window=100, long_window=400)
signals = mac.generate_signals()

print(signals)

portfolio = MarketOnClosePortfolio(df, signals, initial_capital=10000)

print(portfolio)
\
# mavg = Series(df).rolling(window=40, center=False).mean()
# mavg = pd.rolling_mean(df['Close'], 40)
# mavg.plot(label='mavg')
# plt.legend()
# mavg = pd.rolling_mean(df['Close'], 40)
# print(mavg[-10:])

# This line is necessary for the plot to appear in a Jupyter notebook
# % matplotlib inline
# Control the default size of figures in this Jupyter notebook
# % pylab inline
# pylab.rcParams['figure.figsize'] = (15, 9)  # Change the size of plots

#df['Adj Close'].plot(grid=True)
# df['Emwa'] = pd.ewma(df['Close'],span=60,freq='D')
# df['SMA']  = indicators.simple_moving_average(df, 4)
#df['EWMA']  = indicators.exponential_moving_average(df['Close'], 26)
#df['EMA']  = indicators.exponential_moving_average(df['Close'], 14)

#df['MACD'], df['Signal'], df['Histogram'] = indicators.moving_average_convergence_divergence(df['Close'])
#print(df['MACD'])

#df['MACD'].plot(grid=True)
#plt.show()
#print(df['EWMA'])
#print(df['EMA'])


#plt.show()

# df['SMA'] = df['Close'].ewm()
# print(df['SMA'])
# df['EWMA'].plot(grid=True)
# df['SMA'].plot(grid=True)
# mavg = pd.ewma(df['Close'])
# mavg.plot(grid=True)

# df['RSI'] = indicators.relative_strength_index(df['Close'])

# df['RSI'].plot(grid=True)
# plt.show()

# print(df['RSI'])

#df["ADX"] = indicators.average_directional_index(df, 14)
#df['ADX'].plot(grid=True)
#plt.show()

# print(df["ADX"])

