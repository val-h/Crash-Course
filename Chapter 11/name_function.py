#first = input('First name: ')
#middle = input('Middle name: ')
#last = input('Last name: ')

def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = f'{first} {middle} {last}'
    else:
        full_name = f'{first} {last}'
    return full_name.title()

#print(get_formatted_name(first, last))
