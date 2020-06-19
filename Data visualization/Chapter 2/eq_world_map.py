from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

from eq_explore_data import EarthquakeData

# Create an instance and pass the disered filepaths, or leave the default
eq = EarthquakeData()
eq.Details()

# Map the earthquakes
eq_data = [{
    'type': 'scattergeo',
    'lon': eq.lons,
    'lat': eq.lats,
    'marker': {
        'size': [5*mag for mag in eq.mags if mag > 0],
        'color': 'red',
    },
}]

# Styling and layout
custom_layout = Layout(title='Global Earthquakes')

fig = {'data': eq_data, 'layout': custom_layout}
offline.plot(fig, filename='Data visualization\\Chapter 2\\eq_map.html')
