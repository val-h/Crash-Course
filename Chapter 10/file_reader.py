filepath = 'Chapter 10\\text files\\pi_million_digits.txt'
with open(filepath) as file_object:
    lines = file_object.readlines()

pi = ''

for line in lines:
    pi+= line.strip()

print(f'The number pi: {pi[:52]}\nTotal lenght {len(pi)}')

birthday = input('Enter your birthday(fromat: ddmmyy) - ')
if birthday in pi:
    print(f'Yes! The date {birthday} is contained in pi.')
else:
    print(f'No. The date {birthday} is not contained in pi.')
