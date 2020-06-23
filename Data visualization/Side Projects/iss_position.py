# Visualizing the position of the ISS through API call

import requests

from plotly.graph_objs import Scattergeo
from plotly import offline

def APICall():
    url = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(url)
    print(f'API Call - Status code: {response.status_code}')
    data_dict = response.json()

    lon = (float(data_dict['iss_position']['longitude']),)  # tuple
    lat = (float(data_dict['iss_position']['latitude']),)   # tuple
    return lon, lat

def VIsualizingISS(lon, lat):
    """Visualizing the ISS on the map"""

    data = {
        'type': 'scattergeo',
        'lon': lon,
        'lat': lat,
        'hovertext': 'International Space Station',
        'marker': {
            'size': 40,
            'color': 'green',
            'line': {'width': 3, 'color': 'yellow'}
        }
    }

    cst_layout = {
        'title': 'ISS Position',
        'xaxis': {'title': 'Longitude'},
        'yaxis': {'title': 'Latitude'},
    }

    figure = {'data': data, 'layout': cst_layout}

    offline.plot(figure, filename='iss_position.html')

def main():
    lon, lat = APICall()
    VIsualizingISS(lon, lat)

if __name__ == '__main__':
    main()