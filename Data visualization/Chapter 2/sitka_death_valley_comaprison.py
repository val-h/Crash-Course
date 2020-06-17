import csv

from matplotlib import pyplot as plt
from datetime import datetime as dt

sitka_filename = 'Data visualization\\Chapter 2\\data\\sitka_weather_2018_simple.csv'
death_valley_filename = 'Data visualization\\Chapter 2\\data\\death_valley_2018_simple.csv'

# Sitka data
with open(sitka_filename) as f:
    csv_data_sitka = csv.reader(f)
    sitka_header_data = next(csv_data_sitka)

    for i, data in sitka_header_data:
        print(i, data)
        if data == 'NAME':
            s_name_index = i 
        if data == 'DATE':
            s_date_index = i
        if data == 'TMAX':
            s_tmax_index = i
        if data == 'TMIN':
            s_tmin_index = i 

    # Data lists
    highs = []
    lows = []
    dates = []

    # Data athering loop
    for row in csv_data_sitka:
        date = dt.strptime(csv_data_sitka[s_date_index])
        try:
            high_t = int(row[s_tmax_index])
            low_t = int(row[s_tmin_index])
        except ValueError:
            print(f'Missing Value for {date}!')
        else:
            dates.append(date)
            highs.append(high_t)
            lows.append(low_t)

# TODO, finish the visualization

# Death valley data
with open(death_valley_filename) as f:
    csv_data_death_valley = csv.reader(f)
    death_valley_header_data = next(csv_data_death_valley)

print('Index-Sitka-Death_Valley')
for i in range(len(sitka_header_data)):
    print(i, sitka_header_data[i],death_valley_header_data[i])

