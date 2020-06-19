import csv
from matplotlib import pyplot as plt
from datetime import datetime as dt

sitka_filename = 'Data visualization\\Chapter 2\\data\\sitka_weather_2018_full.csv'
death_valley_filename = 'Data visualization\\Chapter 2\\data\\death_valley_2018_full.csv'

# Death Valley Weather data
def DataGathering(filename):
    """Function to gather information from a csv file and return 2 lists"""
    with open(filename) as f:
        csv_data = csv.reader(f)
        header_data = next(csv_data)

        for i, data in enumerate(header_data):
            if data == 'DATE':
                date_index = i
            elif data == 'PRCP':
                prcp_index = i
        
        # Data lists
        dates = []
        prcps = []

        # Data loop
        for row in csv_data:
            current_date = dt.strptime(row[date_index], '%Y-%m-%d')
            try:
                prcp = float(row[prcp_index])
            except ValueError:
                print(f'Missing data for {current_date}.')
            else:
                dates.append(current_date)
                prcps.append(prcp)
        
    return dates, prcps

# Visualization
def Visualization():
    dv_dates, dv_prcp = DataGathering(death_valley_filename)
    s_dates, s_prcp = DataGathering(sitka_filename)

    fig, ax = plt.subplots(figsize=(15, 7), dpi=128)

    # Sitka
    ax.plot(s_dates, s_prcp, c='blue', alpha=0.6, label='Sitka Rainfall')

    # Death Valley
    ax.plot(dv_dates, dv_prcp, c='purple', alpha=0.4, label='Death Valley Rainfall')

    # Styling
    ax.set_title('Rainfall in Sitka and Death Valley, 2018', fontsize=24)
    ax.set_xlabel('Dates', fontsize=16)
    ax.set_ylabel('Percentage', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=14)
    fig.autofmt_xdate()

    plt.legend()
    plt.show()

def main():
    Visualization()

if __name__ == '__main__':
    main()
