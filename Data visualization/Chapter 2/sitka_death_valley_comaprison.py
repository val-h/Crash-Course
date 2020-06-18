import csv

from matplotlib import pyplot as plt
from datetime import datetime as dt

sitka_filename = 'Data visualization\\Chapter 2\\data\\sitka_weather_2018_simple.csv'
death_valley_filename = 'Data visualization\\Chapter 2\\data\\death_valley_2018_simple.csv'

# Sitka data
with open(sitka_filename) as f:
    csv_data_sitka = csv.reader(f)
    sitka_header_data = next(csv_data_sitka)

    for i, data in enumerate(sitka_header_data):
        if data == 'DATE':
            s_date_index = i
        if data == 'TMAX':
            s_tmax_index = i
        if data == 'TMIN':
            s_tmin_index = i 

    # Data lists for sitka s_
    s_dates = []
    s_highs = []
    s_lows = []

    # Data gathering loop
    for row in csv_data_sitka:
        date = dt.strptime(row[s_date_index], '%Y-%m-%d')
        try:
            high_t = int(row[s_tmax_index])
            low_t = int(row[s_tmin_index])
        except ValueError:
            print(f'Missing Value for {date}!')
        else:
            s_dates.append(date)
            s_highs.append(high_t)
            s_lows.append(low_t)

# Death valley data
with open(death_valley_filename) as f:
    csv_data_death_valley = csv.reader(f)
    death_valley_header_data = next(csv_data_death_valley)

    for i, data in enumerate(death_valley_header_data):
        if data == 'DATE':
            dv_date_index = i
        elif data == 'TMAX':
            dv_tmax_index = i
        elif data == 'TMIN':
            dv_tmin_index = i

    # Data lists for death valley dv_
    dv_highs = []
    dv_lows = []
    dv_dates = []

    # Data loop
    for row in csv_data_death_valley:
        date = dt.strptime(row[dv_date_index], '%Y-%m-%d')
        try:
            high_t = int(row[dv_tmax_index])
            low_t = int(row[dv_tmin_index])
        except ValueError:
            print(f'Missing data for {date}.')
        else:
            dv_dates.append(date)
            dv_highs.append(high_t)
            dv_lows.append(low_t)

# Visualization

plt.style.use('seaborn-dark')
fig, ax = plt.subplots(figsize=(15, 7), dpi=128)

# Sitka plots
ax.plot(s_dates, s_highs, c='red', alpha=0.4, label='Sitka Highs')
ax.plot(s_dates, s_lows, c='blue', alpha=0.6 ,label='Sitka Lows')
ax.fill_between(s_dates, s_highs, s_lows, facecolor='orange', alpha=0.2)

# Death Valley plots
ax.plot(dv_dates, dv_highs, c='red', alpha=0.6, label='Death Valley Highs')
ax.plot(dv_dates, dv_lows, c='blue', alpha=0.4, label='Death Valley Lows')
ax.fill_between(dv_dates, dv_highs, dv_lows, facecolor='purple', alpha=0.2)

plt.legend()
plt.show()

# A lot of code could be refactored, just make 2 functions.
# One function for the csv file extractor with 3 lists as return
# And the other one for visualizing the data, 1 complete plot as return
