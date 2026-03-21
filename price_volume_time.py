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


data['Datetime'] = pd.to_datetime(data['Datetime']).dt.tz_localize(None)


'''
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data['Datetime'], data['Close'])

ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax.xaxis.set_major_locator(mdates.MonthLocator())
plt.xticks(rotation=45)



plt.show()
'''


fig, ax = plt.subplots(figsize = (10,6))

# Set up the plot limits so the animation doesn't "jump"
ax.set_xlim(data['Datetime'].min(), data['Datetime'].max())
ax.set_ylim(data['Close'].min() * 0.98, data['Close'].max() * 1.02)

### axis formatting

ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax.xaxis.set_major_locator(mdates.MonthLocator())
plt.xticks(rotation=45)


l, = plt.plot([], [], 'r-')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title(ticker)

xlist = []
ylist = []

metadata = dict(title='Movie', artist='dandelion')
writer = PillowWriter(fps=40, metadata=metadata)

with writer.saving(fig, "stock.gif", 100):
    for i in range(0,len(data), 2):
        xlist = data['Datetime'].iloc[:i]
        ylist = data['Close'].iloc[:i]

        l.set_data(xlist, ylist)

        writer.grab_frame()
