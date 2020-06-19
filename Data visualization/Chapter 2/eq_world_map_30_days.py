from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

from eq_explore_data import EarthquakeData as EqData

# Filepaths needed for the EqData instance
raw_file = 'Data visualization\\Chapter 2\\data\\all_month.geojson.json'
ref_file = 'Data visualization\\Chapter 2\\data\\ref_all_month.geojson.json'

eq = EqData(raw_file, ref_file)
eq.Details()

# Data for scattergeo
data = [{
    'type':'scattergeo',
    'lon': eq.lons,
    'lat': eq.lats,
    'text': eq.hover_texts,
    'marker': {
        'size': [5*mag for mag in eq.mags if mag > 0],
        'color': eq.mags,
        'colorscale': 'Reds',
        #'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    }
}]

# Styling and Layout
title = eq.title + ' ,19/6/2020'
custom_layout = Layout(title=title)

fig = {'data': data, 'layout': custom_layout}
offline.plot(fig,
 filename='Data visualization\\Chapter 2\\eq_map_30_days.py.html')
