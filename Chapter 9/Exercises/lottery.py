from random import randint

"""Lottery game. 6/46"""

# 6 numbers in range 1- 46
my_ticket = [int(x) for x in input('Write 6 numbers for you ticket(Sep with space)- ').split()]
tested_tickets = []

def ticket():
    """Creating a simple ticket."""
    ticket = []
    while len(ticket) < 6:
        lucky_num = randint(1, 46)
        if lucky_num not in ticket:
            ticket.append(lucky_num)
    return ticket

# Lottery time
print('Starting the lottery...')
while True:
    tested_tickets.append(ticket())
    if sorted(my_ticket) == sorted(tested_tickets[-1]):
        break

print(f'We have a Winner! - {tested_tickets[-1]}')
print(f'Number of tested tickets - {len(tested_tickets)}')

show_tickets = input('Do you want to print all of the tested tickets? Type \'y\' - ').lower()
if show_tickets == 'y':
    for i, ticket in enumerate(tested_tickets):
        print(f'Ticket N{i + 1} - {ticket}')

print('Quiting program.')
