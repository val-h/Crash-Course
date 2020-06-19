import json

from plotly.graph_objs import Scattergeo, Layout 
from plotly import offline

filepath = 'Data visualization\\Chapter 2\\data\\significant_eqs.geojson.json'

class EarthquakeData:

    def __init__(self, filepath=filepath):
        """Read through a json file and create lists based on it"""

        with open(filepath) as f:
            all_dict_data = json.load(f)

        with open(filepath, 'w') as f:
            json.dump(all_dict_data, f, indent=4)

        self.all_eq_data = all_dict_data['features']
        self.title = all_dict_data['metadata']['title']
        self.loaded_earthquakes = 0
        self.missing_data = 0

        # Creating the magnitude, longitude, latitude and hover text lists
        self.mags, self.lons, self.lats, self.hover_texts = [], [], [], []

        # Going through each earthquake('feature') and extracting data
        # from the nested dictionaries
        for eq_dict in self.all_eq_data:
            mag = eq_dict['properties']['mag']
            lon = eq_dict['geometry']['coordinates'][0]
            lat = eq_dict['geometry']['coordinates'][1]
            hover_text = eq_dict['properties']['title']
            # Checking if the magnitude is a valid variable, if it is a float
            # and not a NoneType, not needed here for this specific file
            if mag:
                self.mags.append(mag)
                self.lons.append(lon)
                self.lats.append(lat)
                self.hover_texts.append(hover_text)
                self.loaded_earthquakes += 1
            else:
                print(f'Missing data for earthquake {eq_dict.index() + 1}.')
                self.missing_data += 1
    
    def CreatingPlot(self):
        """Visualizing the data generated in the init method"""

        # Customize the data set
        data = [{
            'type': 'scattergeo',
            'lon': self.lons,
            'lat': self.lats,
            'text': self.hover_texts,
            'marker': {
                'size': [7*mag for mag in self.mags],
                'color': self.mags,
                'colorscale': 'Reds',
                'colorbar': {'title': 'Magnitude'},
            }
        }]

        # Layout
        custom_layout = Layout(title=self.title)

        # Creating the figure and file with the plot
        figure = {'data': data, 'layout':custom_layout}
        offline.plot(figure, filename='major_earthquakes.html')

    def Details(self):
        """Details about this instance"""

        print(f'Title of the document - {self.title}')
        print(f'Total dictionaries - {len(self.all_eq_data)}')
        print(f'Loaded(visualized) earthquakes - {self.loaded_earthquakes}')
        print(f'Missing data - {self.missing_data}')

        max_mag = 0.0
        min_mag = 20.0
        for magnitude in self.mags:
            max_mag = max(max_mag, magnitude)
            min_mag = min(min_mag, magnitude)
        
        print(f'Maximum magnitude - {max_mag}')
        print(f'Minimum magnitude - {min_mag}')

if __name__ == '__main__':
    eq = EarthquakeData(filepath)        
    eq.Details()
    eq.CreatingPlot()
