import requests
import json

# Create the request object and print the data
url = 'https://api.github.com/search/repositories?q=language:python&sort:stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

response_dict = r.json()
print(response_dict.keys())
print(f'Total count: {response_dict["total_count"]}')

# Explore information about the repositories
repo_dicts = response_dict['items']
print(f'Total repos returned: {len(repo_dicts)}')

# Examine the information about the returned repositories 
print(f'\nSelected information about the first repository:')
for repo_dict in repo_dicts:
    print(f'\nName - {repo_dict["name"]}')
    print(f'Owner - {repo_dict["owner"]["login"]}')
    print(f'Stars - {repo_dict["stargazers_count"]}')
    print(f'Repository - {repo_dict["html_url"]}')
    print(f'Description - {repo_dict["description"]}')
