from datetime import datetime as dt

filepath = 'Chapter 10\\text files\\guests.txt'
names = []

with open(filepath) as file_object:
    for line in file_object.readlines():
        names.append(line.rstrip().split('-'))

def AddGuest(name):
    """Adding a guest name to a specific file."""
    i = str(len(names) + 1)
    #date = dt.utcnow()
    #date = dt.strftime('%d%m%Y', date)
    with open(filepath, 'a') as file_object:
        file_object.write(i + '-' + name + '\n')

name = input('Name? - ').lower()

if name not in names:
    print(f'{name.title()}, you are not in the list... Please come again.')
    AddGuest(name)
else:
    print(f'Last visit: ')
    print(f'{name.title()}! Welcome back.')
