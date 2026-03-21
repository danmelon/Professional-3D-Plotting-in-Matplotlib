import numpy as np
import matplotlib
# matplotlib.use("Agg") # useful for a webserver case where you don't want to ever visualize the result live.
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
import yfinance as yf
import pandas as pd


plt.style.use('dark_background') ## I put this in because I prefer darkmode

ticker = 'TSLA'

data = yf.download(ticker, period="50d", interval="1h", progress=False, auto_adjust=True)
# Clean and prepare data
data['Close'] = data['Close'].astype(float)
data['High'] = data['High'].astype(float)
data['Low'] = data['Low'].astype(float)
data['Open'] = data['Open'].astype(float)
data['Volume'] = data['Volume'].astype(float)

data = data.reset_index()          # brings Datetime in as a column
data.columns = data.columns.get_level_values(0)         # Gets rid of the pesky 'TSLA' label across the second line... i.e. takes just level 0 as labels.


plt.plot(data['Datetime'],data['Close'])
plt.show()