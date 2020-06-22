from operator import itemgetter
from plotly.graph_objs import Bar
from plotly import offline

import requests

# Search the top threads
subm_url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(subm_url)
print('Status code:', r.status_code)

# Going through all of the submissions
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Make a seperate call for each submission
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    sub_r = requests.get(url)
    print(f'id: {submission_id}\tstatus: {sub_r.status_code}')
    response_dict = sub_r.json()

    # Build submission dictionary
    submission_dict = {
        'owner': response_dict['by'],
        'title': response_dict['title'],
        'hn_link': f'https://news.ycombinator.com/item?id={submission_id}',
        'comments': response_dict['descendants'],
        'score': response_dict['score'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Creating the lists for the visualization and printing info about each discussion
comments, names, labels = [], [], []
for submission_dict in submission_dicts:
    print(f'\nTitle - {submission_dict["title"]}')
    print(f'Discussion link - {submission_dict["hn_link"]}')
    print(f'Comments - {submission_dict["comments"]}')
    print(f'Score - {submission_dict["score"]}')

    names.append(f'<a href="{submission_dict["hn_link"]}">{submission_dict["title"]}</a>')
    comments.append(submission_dict['comments'])

    # Create a second visualization based on the users gathered here and their karma
    pt_1 = f'Owner: {submission_dict["owner"]}<br />'
    pt_2 = f'Score: {submission_dict["score"]}<br />'
    labels.append(f'{pt_1}{pt_2}')

# Visualization

data = {
    'type': 'bar',
    'x': names,
    'y': comments,
    'hovertext': labels,
    'marker': {
        'color': 'orange',
        'line': {'width': 2.5, 'color': 'green'},
    },
    'opacity': 0.6,
}

cst_layout = {
    'title': 'Hacker News Top 30 Discussions',
    'xaxis': {
        'title': 'Names',
        'titlefont': {'size': 26},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 26},
        'tickfont': {'size': 14},
    }
}

figure = {'data': data, 'layout': cst_layout}
offline.plot(figure, filename='hn_top_30.html')
