import numpy as np
import matplotlib
# matplotlib.use("Agg") # useful for a webserver case where you don't want to ever visualize the result live.
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
import yfinance as yf
import pandas as pd
import matplotlib.dates as mdates


plt.style.use('dark_background') ## I put this in because I prefer darkmode

ticker = 'TSLA'

data = yf.download(ticker, period="50d", interval="1h", progress=False, auto_adjust=True)
# Clean and prepare
data = data.reset_index()          # brings Datetime in as a column
data.columns = data.columns.get_level_values(0)         # Gets rid of the pesky 'TSLA' label across the second line... i.e. takes just level 0 as labels.


data['DateNum'] = mdates.date2num(data['Datetime'])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

plt.xticks(rotation=45)

plt.xlabel('Date')
plt.ylabel('Price')
plt.title(ticker)

x = data['DateNum']
y = data['Close']
z = data['Volume']

# Plotting a 3D line instead of a surface (which requires a matrix)
ax.plot(x, y, z, color='cyan', lw=2)

### axis formatting

ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax.xaxis.set_major_locator(mdates.MonthLocator())

ax.set_xlabel('Date')
ax.set_ylabel('Price ($)')
ax.set_zlabel('Volume')
plt.title(f'{ticker} Price vs Volume')

plt.show()

