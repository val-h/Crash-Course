import csv
from matplotlib import pyplot as plt
from datetime import datetime as dt

ni_weather_file = 'Data visualization\\Chapter 2\\data\\ni_weather_data.csv'

def CsvDataExtractor(filename):
    """
    Function to extract data from a csv file,
    Returns 3 lists - dates, air_temperature, sea_temperature
    """

    with open(filename) as f:
        csv_data = csv.reader(f)
        header_data = next(csv_data)

        for i, data in enumerate(header_data):
            if data == 'time':
                time_index = i
            #elif data =='WindSpeed':
            #    wind_speed_index = i
            elif data == 'AirTemperature':
                air_temperature_index = i
            elif data == 'SeaTemperature':
                sea_temperature_index = i
        
        # Storing the data
        dates = []
        #wind_speeds = []
        air_temperatures = []
        sea_temperatures = []

        # Data loop
        for row in csv_data:
            if '13:00' in row[time_index]:
                current_time = dt.strptime(row[time_index], '%Y-%m-%dT%H:%M:%SZ')
                try:
                    #wind_speed = float(row[wind_speed_index])
                    air_temperature = float(row[air_temperature_index])
                    sea_temperature = float(row[sea_temperature_index])
                except ValueError:
                    print(f'Missing data for {current_time}')
                else:
                    dates.append(current_time)
                    #wind_speeds.append(wind_speed)
                    air_temperatures.append(air_temperature)
                    sea_temperatures.append(sea_temperature)
    
    return dates, air_temperatures, sea_temperatures

def Visualization():
    """Visualization for the weather data"""
    # Dates, wind speed, air temperature, sea temperature
    dates, at, st = CsvDataExtractor(ni_weather_file)

    fig, ax = plt.subplots(figsize=(15,7), dpi=128)
    
    # Plotting the data
    #ax.plot(dates, ws, c='green', alpha=0.6, label='Wind speed')
    ax.plot(dates, at, c='red', alpha=0.6, label='Air temperature')
    ax.plot(dates, st, c='blue', alpha=0.6, label='Sea temperature')
    #ax.fill_between(dates, at, st, facecolor='purple', alpha=0.2, 
    #label='Temperature difference')

    # Styling
    ax.set_title('Ni weather data since 2001', fontsize=26)
    ax.set_xlabel('Dates', fontsize=16)
    ax.set_ylabel('Temperatures (C)', fontsize=16)
    ax.tick_params(axis='y', which='major', labelsize=14)
    fig.autofmt_xdate()

    # Creating the graph
    plt.legend()
    plt.show()

def main():
    Visualization()

if __name__ == '__main__':
    main()
