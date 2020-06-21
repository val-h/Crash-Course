import requests
import json

# Make an API call and store the response
url = 'https://hacker-news.firebaseio.com/v0/item/23593872.json'
r = requests.get(url)
print(r.status_code)

# Explore the structure of the data
filepath = 'Data visualization\\data\\hn_article.json'
response_dict = r.json()
with open(filepath, 'w') as f:
    json.dump(response_dict, f, indent=4)
