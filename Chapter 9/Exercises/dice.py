from random import randint

"""Dice program. : )"""

print('\nWelcome to the dice program...')
print('Type \'r\' to roll the dice or \'q\' to quit')
while True:
    cmd = input('/> ').lower()
    if cmd == 'q':
        print('Quiting program...')
        quit()
    elif cmd == 'r':
        print(f'You rolled {randint(1, 6)}')
    else:
        print('Error! Wrong command.')
