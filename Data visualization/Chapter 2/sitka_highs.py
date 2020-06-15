import csv
from matplotlib import pyplot as plt
from datetime import datetime as dt

filename = 'Data visualization\\Chapter 2\\data\\sitka_weather_07-2018_simple.csv'

with open(filename) as f:
    csv_data = csv.reader(f)
    header_row = next(csv_data)

    for i, data in enumerate(header_row):
        print(i, data)
    
    # Going through the lines of data and storing the max temp in a list
    highs = []
    dates = []
    for row in csv_data:
        # Temperature
        high_t = int(row[5])
        highs.append(high_t)
        
        # Date
        date_str = row[2]
        date = dt.strptime(date_str, '%Y-%m-%d')
        dates.append(date)

# Creating the visualization

# TODO - Add the Low temperature as well and improve the visualization

plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(14, 8), dpi=128)

ax.plot(dates, highs, c='red', label='Temperature')

ax.set_title('Daily high temperatures, Sitka AK, July 2018', fontsize=26)
ax.set_xlabel('Date', fontsize=16)
ax.set_ylabel('Temperature (F)', fontsize=16)

ax.tick_params(axis='both', which='major', labelsize=14)
#ax.tick_params(axis='x', which='major', labelsize=8, labelrotation=45)
fig.autofmt_xdate() # This is a better version than the one above ^

plt.legend()
plt.show()
