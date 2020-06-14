import csv

filename = 'Data visualization\\Chapter 2\\data\\sitka_weather_07-2018_simple.csv'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
