import json 

filepath = 'usernames.json' # Chapter 10\json files\usernames.json
try:
    with open(filepath) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input('Please write your username: ')
    print(f'We will remember you the next time you come back, {username}!')
    with open(filepath, 'w') as f:
        json.dump(username, f)
except ValueError:
    username = input('Please write your username: ')
    print(f'We will remember you the next time you come back, {username}!')
    with open(filepath, 'w') as f:
        json.dump(username, f)
else:
    print(f'Welcome back, {username}!')
