from essentials import update_value
from car import Car
from electric_car import ElectricCar

words_for_exit = ['q', 'quit', 'exit', 'end', 'stop', 'yamero']
car_options = ['car', 'electric car']
prompt = '\n/> '    # an extra line of code

# Add new commands as the project grows
commands = ['name', 'r_odo', 'u_odo', 'i_odo', 'battery', 'range', 'r_bl', 'u_bl']
other_commands = ['help']

# Module functions
def available_cars():
    """
    Printing the available cars.
    """
    print('Please choose one of the available cars:')
    for car in car_options:
        print(f'\t{car}')

def openning_message():
    """
    Openning message for the user when he uses the program for the first time.
    """
    # More updates later
    print('\n Welcome to my simple car project! Take your time and explore.')
    print('Since you don\'t have a car you will have to create one...')
    available_cars()

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
    
def command_exe(cmd):
    """
    A more organised way for the command excutions.
    Takes one 'command input' and checks it with the
    available commands.
    """
    if cmd in words_for_exit:
        print('Program shutting down...')
        quit()

    # General car commands
    if cmd == 'name':
        print(my_car.descriptive_name())
    elif cmd == 'r_odo':
        my_car.read_odometer()
    elif cmd == 'u_odo':
        my_car.update_odometer()
    elif cmd == 'i_odo':
        my_car.increment_odometer()
    
    # Electric car commands
    elif cmd in commands and car_type == 'electric car':
        if cmd == 'battery':
            my_car.battery.describe_battery()
        elif cmd == 'range':
            my_car.battery.get_range()
        elif cmd == 'r_bl':
            my_car.battery.read_battery()
        elif cmd == 'u_bl':
            my_car.battery.update_battery()
    
    # Other commands
    elif cmd == 'help':
        help()
    
    # Error message
    else:
        if cmd not in commands and cmd not in other_commands:
            print(f'\nError! {cmd} is not a valid command.')
            print('Type \'help\' for a list of commands.')
        else:
            print(f'{cmd} is not a valid command  for \'{car_type}\'.')

def help():
    print('\nThis is a list with all the available commands:')
    for command in commands:
        print(f' - {command}')
    for command in other_commands:
        print(f' - {command}')

#
# A lot more could be done with this - login -> check garage -> review profile
# earn money by playing mini games -> spent curency on stuff -> save progress.
#

# Opening of the program
openning_message()
my_car = None
car_type = ''

# Car creation
while my_car == None:
    cmd = input(prompt).lower()
    if cmd == 'car' or cmd == 'electric car':
        car_type = cmd
        make = input('Car make: ')
        model = input('Car model: ')
        year = int(update_value('year of the car')) # it returns a float value : /
        my_car = create_car(car_type, make, model, year)
    else:
        print('Error!')
        available_cars()

print('\nYou can now work with the car\'s parameters and information')

# User commands loop
while True:
    
    # User inp
    cmd = input(prompt).lower()

    # Command check
    command_exe(cmd)
