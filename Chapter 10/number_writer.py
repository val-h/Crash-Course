import json

filepath = 'Chapter 10\\json files\\numbers.json'
numbers = input('Enter a sequence of numbers: ').split()

with open(filepath, 'w') as f:
    json.dump(numbers, f)

with open(filepath, 'r') as f:
    print(json.load(f))
