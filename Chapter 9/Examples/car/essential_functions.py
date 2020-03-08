from car import Car
from electric_car import ElectricCar


"""A file containing the essential functions used in this program."""

def create_car(car_type, make, model, year):
    """
    Creates the car object for the program depending on the user input.
    """
    if car_type == 'car':
        car = Car(make, model, year)
    elif car_type == 'electric car':
        car = ElectricCar(make, model, year)
    print(f'\n{car_type.title()} {make.title()} was successfuly created!')
    return car

def update_value(value_name):
    """
    Asks the user for a positive value until it gets one.
    Requires a string parameter for the input message in format:
            Value for {value_name}: 
    """
    while True:
        try:
            temp_value = float(input(f'Value for {value_name}: '))
        except:
            print('Please write a number...')
        else:
            if temp_value <= 0:
                print('Please write a positive number.....')
                continue
            else:
                break
    return temp_value
