import csv
from matplotlib import pyplot as plt
from datetime import datetime as dt

sitka_filename = 'Data visualization\\Chapter 2\\data\\sitka_weather_2018_full.csv'
death_valley_filename = 'Data visualization\\Chapter 2\\data\\death_valley_2018_full.csv'

# Sitka weather data
with open(sitka_filename) as f:
    s_csv_data = csv.reader(f)
    s_header_data = next(s_csv_data)

    for i, data in enumerate(s_header_data):
        if data == 'DATE':
            s_date_index = i
        elif data == 'PRCP':
            s_prcp_index = i
        elif data == 'SNOW':
            s_snwd_index = i
    
    # Data lists
    s_dates = []
    s_prcp = []
    s_snwd = []

    # Data loop
    for row in s_csv_data:
        current_date = dt.strptime(row[s_date_index], '%Y-%m-%d')
        try:
            prcp = float(row[s_prcp_index])
            snwd = float(row[s_snwd_index])
        except:
            print(f'Missing data for {current_date}.')
        else:
            s_dates.append(current_date)
            s_prcp.append(prcp)
            s_snwd.append(snwd)

# Death Valley Weather data
with open(death_valley_filename) as f:
    dv_csv_data = csv.reader(f)
    dv_header_data = next(dv_csv_data)

    for i, data in enumerate(dv_header_data):
        pass
        # TODO, finishe this and this time no interactive bs, just make a 
        # static method that returns the 3 desired lists from both files
        # from a single function, and a singel function for visualization!

def main():
    pass

if __name__ == '__main__':
    main()
