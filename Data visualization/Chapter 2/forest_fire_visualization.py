import csv

from plotly.graph_objs import Scattergeo, Layout 
from plotly import offline
from datetime import datetime as dt

filepath = 'Data visualization\\Chapter 2\\data\\fires_world_24h.csv'

class ForestFireData:
    """Class to generate, hold and visualize fires in the world"""

    def __init__(self, filepath=filepath):
        """Load the csv file and extract data from it"""

        with open(filepath) as f:
            csv_data = csv.reader(f)
            header_data = next(csv_data)

            for i, data in enumerate(header_data):
                if data == 'latitude':
                    latitude_index = i
                elif data == 'longitude':
                    longitude_index = i
                elif data == 'bright_ti4':
                    b_temp_index = i
                elif data == 'acq_date':
                    date_index = i
                elif data == 'acq_time':
                    time_index = i
                elif data == 'daynight':
                    day_night_index = i
            
            # Creating the lists for the data
            self.lats, self.lons, self.b_temps, self.texts = [], [], [], []
            self.dates = []

            # Going through each fire
            for row in csv_data:
                lat = row[latitude_index]
                lon = row[longitude_index]
                b_temp = float(row[b_temp_index])
                date = dt.strptime(f'{row[date_index]}{row[time_index]}',
                 '%Y-%m-%d%H%M')
                d_n = row[day_night_index]
                text = f'Discovered: {date}, time of day: {d_n}'
                if b_temp - 273.15 > 0:
                    self.lats.append(lat)
                    self.lons.append(lon)
                    self.b_temps.append(b_temp - 273.15)
                    self.dates.append(date)
                    self.texts.append(text)
                else:
                    print(f'Invalid data for {date}.')
    
    def CreateVisualization(self):
        """Create the data, layout and figure. Visualize the fires"""

        # Setting the data for the visualization
        data = [{
            'type': 'scattergeo',
            'lat': self.lats,
            'lon': self.lons,
            'text': self.texts,
            'marker': {
                'size': [b // 3 for b in self.b_temps],
                'color': self.b_temps,
                'colorscale': 'Reds',
                'colorbar': {'title': 'Brightness Temperature (C)'}
            }
        }]

        # Creating the layout for the visualization
        title = 'Forest Fires in the world, for te pas 24 hours.'
        custom_layout = Layout(title=title)

        # Creating the figure and plot
        figure = {'data': data, 'layout': custom_layout}
        offline.plot(figure, filename='fires_world_24h.html')

    def Details(self):
        """Details about the fires in the world for the previous 24 h"""

        print(f'Total fires - {len(self.b_temps)}')

if __name__ == '__main__':
    ff = ForestFireData()
    ff.Details()
    ff.CreateVisualization()
