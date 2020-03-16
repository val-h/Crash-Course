from datetime import datetime as dt

filepath_users = 'Chapter 10\\text files\\guests.txt'
filepath_responses = 'Chapter 10\\text files\\responses.txt'
users = {}

class User:
    """User object with a few basic arguments."""

    def __init__(self, id, name, date):

        self.id = id
        self.name = name
        self.date = date

with open(filepath_users) as file_object:
    for line in file_object.readlines():
        user_info = line.rstrip().split('-')
        users[user_info[1]] = (User(user_info[0], user_info[1], user_info[2]))

def AddGuest(name):
    """Adding a guest name to a specific file."""
    i = str(len(users) + 1)
    date = dt.utcnow()
    date = date.strftime('%d/%b/%Y')
    user_info = f'{i}-{name}-{date}'
    with open(filepath_users, 'a') as file_object:
        file_object.write(user_info + '\n')

while True:
    name = input('Name? - ').lower()
    if name == 'q':
        print('Quiting...')
        break

    if name not in users:
        print(f'{name.title()}, you are not in the list... Please come again.')
        AddGuest(name)
    else:
        print(f'Last visit of id{users[name].id}: {users[name].date}')
        print(f'{name.title()}! Welcome back.')
        cmd = input('Why do  you like programming? - ')
        with open(filepath_responses, 'a') as file_object:
            file_object.write(cmd + '\n')
        print('Response added!')
