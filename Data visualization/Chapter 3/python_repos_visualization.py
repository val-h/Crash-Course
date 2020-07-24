import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make API call to github about the top Python repositories(by stars)
language = 'python'
url = f'https://api.github.com/search/repositories?q=language:{language}&sort:stars'
headers = {'Accepted': 'application/vnd.github.v3+json'} # Specifying the api version
r = requests.get(url, headers=headers) # Assign the request object
print('Status code: ', r.status_code) # 200 - accepted, check mozilla http request codes

# Process results
response_dict = r.json() # Loads the variable with the data 
repo_dicts = response_dict['items'] # Store each of the repositories

# Lists to hold the desired data for the plot
repo_links, repo_stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']

    # Picking the repo url and adding it to the x label
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    repo_stars.append(repo_dict['stargazers_count'])

    # Label with owner and description for the bars of the chart
    owner = repo_dict["owner"]["login"]
    desc = repo_dict['description']
    labels.append(f'{owner}<br />{desc}')

# Visualization
data = {
    'type': 'bar',
    'x': repo_links,
    'y': repo_stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 150, 100)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6

}
cst_layout = {
    'title': 'Top Python repositories in GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    }
}

figure = {'data': data, 'layout': cst_layout}
offline.plot(figure, filename='python_top_repos.html')
