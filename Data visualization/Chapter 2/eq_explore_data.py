import json

raw_file = 'Data visualization\\Chapter 2\\data\\all_day.geojson.json'
ref_file = 'Data visualization\\Chapter 2\\data\\ref_eqrthquakes.geojson.json'

class EarthquakeData:
    """A class to represent specific earthquake data"""

    # Could be done with only one file, keeping it for extra work if needed
    def __init__(self, raw_file=raw_file, ref_file=ref_file):
        """
        Load data from a json file and refactor the data to another file
        Extract all the earthquakes in the 'features' dictionary
        Returns 3 lists, magnitudes, longitudes, latitudes
        """
        with open(raw_file) as f:
            all_eq_data = json.load(f)

        with open(ref_file, 'w') as f:
            json.dump(all_eq_data, f, indent=4)

        self.title = all_eq_data['metadata']['title']
        self.all_eq_dict = all_eq_data['features']
        self.missing_data = 0
        self.total_eqs = 0

        self.mags, self.lons, self.lats, self.hover_texts = [], [], [], []
        for eq_dict in self.all_eq_dict:
            mag = eq_dict['properties']['mag']
            lon = eq_dict['geometry']['coordinates'][0]
            lat = eq_dict['geometry']['coordinates'][1]
            title = eq_dict['properties']['title']
            if mag:
                self.mags.append(mag)
                self.lons.append(lon)
                self.lats.append(lat)
                self.hover_texts.append(title)
                self.total_eqs += 1
            else:
                print(f'Missing data.')
                self.missing_data += 1
        
    def Details(self):
        """Details about the earthquake data"""

        print(f'Total features(dictionaries) - {len(self.all_eq_dict)}')
        print(f'Total eqarthquakes - {self.total_eqs}')
        print(f'Missing data - {self.missing_data}')

        max_mag = 0.0
        min_mag = 20.0
        for magnitude in self.mags:
            max_mag = max(max_mag, magnitude)
            min_mag = min(min_mag, magnitude)

        print(f'Maximum magnitude detected - {max_mag}')
        print(f'Minumum magnitude detected - {min_mag}')

if __name__ == '__main__':
    eq = EarthquakeData()
    eq.Details()
