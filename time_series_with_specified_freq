import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Data points
testQ_data_points = [add data points]

# Create a date range starting from specified date range, with weekly frequency
dates = pd.date_range(start='insert date', periods=len(testQ_data_points), freq='W')

# Create a DataFrame with the date range and data points
data = pd.DataFrame({'Date': dates, 'Value': testQ_data_points})

# Calculate the trend line using numpy's polyfit function
slope, intercept = np.polyfit(np.arange(len(testQ_data_points)), testQ_data_points, 1)
trend_line = slope * np.arange(len(testQ_data_points)) + intercept

# Create the time series chart
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(data['Date'], data['Value'], marker='o', label='Data Points')
ax.plot(data['Date'], trend_line, color='red', label='Trend Line')

# Format the x-axis to display dates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Days')
plt.title('testQ (date range)')
plt.legend()

# Show the plot
plt.show()
