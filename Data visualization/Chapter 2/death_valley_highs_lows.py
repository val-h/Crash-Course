import csv

from datetime import datetime as dt
from matplotlib import pyplot as plt

filename = 'Data visualization\\Chapter 2\\data\\death_valley_2018_simple.csv'

with open(filename) as f:
    csv_data = csv.reader(f)
    header_line = next(csv_data)

    for i, data in enumerate(header_line):
        print(i, data)

    # Lists to hold the specific type of data
    highs = []
    lows = []
    dates = []

    # Loop through the data
    for row in csv_data:
        # Date
        current_date = dt.strptime(row[2], '%Y-%m-%d')
        try:
            high_t = int(row[4])
            low_t = int(row[5])
        except ValueError:
            print(f'Missing data for {current_date}.')
        else:
            dates.append(current_date)
            highs.append(high_t)
            lows.append(low_t)

# Creating the viwsualization
#plt.style.use('seaborn-dark')
fig, ax = plt.subplots(figsize=(15, 7), dpi=128)

ax.plot(dates, highs, c='red', label='Highs', alpha=0.4)
ax.plot(dates, lows, c='blue', label='Lows', alpha=0.4)
ax.fill_between(dates, highs, lows, facecolor='orange', alpha=0.1)

title = 'Daily high and low temperatures - 2018\nDeath Valley, CA'

ax.set_title(title, fontsize=24)
ax.set_xlabel('Dates', fontsize=14)
ax.set_ylabel('Temperature (F)', fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=16)
fig.autofmt_xdate()

plt.legend()
plt.show()
