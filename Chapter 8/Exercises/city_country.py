city = input('City: ')
country = input('Country: ')

def residence_format(city, country):
    residence = f'{city}, {country}'
    return residence.title()

print(residence_format(city, country))
