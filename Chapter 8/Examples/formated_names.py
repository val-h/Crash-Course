f_name = input('First name: ')
m_name = input('Middle name: ')
l_name = input('Last name: ')

def name_format(first, last, middle=''):
    """Craeting a full name and formating it."""
    if middle:
        full_name = f'{first} {middle} {last}'
    else:
        full_name = f'{first} {last}'
    return full_name.title()

print(name_format(f_name, l_name, m_name))
