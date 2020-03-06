
def greeting(first, last):
    """Display a simple greeting."""
    greeting = f'Hello, {first} {last}!'
    return greeting.title()

# Loop for input
while True:
    print('\nPlease tell me your name.')
    f_name = input('First name: ')
    if f_name == 'q':
        break
    l_name = input('Last name: ')
    if l_name == 'q':
        break
    print(greeting(f_name, l_name))
