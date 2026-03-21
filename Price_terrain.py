import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

# 1. Get Data
ticker = 'TSLA'
data = yf.download(ticker, period="20d", interval="1h", progress=False, auto_adjust=True)
data = data.reset_index()
data.columns = data.columns.get_level_values(0)


# 2. Prep for 3D: Create "Hour" and "Date" columns
data['Hour'] = data['Datetime'].dt.hour
data['Date'] = data['Datetime'].dt.date

# 3. Pivot the data to create a Z-matrix (Hours vs Dates)
# This creates the grid needed for plot_surface
pivot_df = data.pivot(index='Date', columns='Hour', values='Close')


# 4. Create the X and Y meshgrid based on the pivot table shape
X, Y = np.meshgrid(pivot_df.columns, np.arange(len(pivot_df.index)))
Z = pivot_df.values

# 5. Plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Use plot_surface now that Z is a 2D matrix!
surf = ax.plot_surface(X, Y, Z, cmap='ocean', edgecolor='none', alpha=0.9)

ax.set_title(f"{ticker} Hourly Price Terrain (Last 20 Days)")
ax.set_xlabel('Hour of Day')
ax.set_ylabel('Days Ago')
ax.set_zlabel('Price ($)')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

plt.show()
