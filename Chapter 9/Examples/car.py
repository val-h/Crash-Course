words_for_exit = ['q', 'quit', 'exit', 'end', 'stop', 'yamero']
car_options = ['car', 'electric car']
prompt = '\n/> '    # an extra line of code

# Add new commands as the project grows
commands = ['name', 'r_odo', 'u_odo', 'i_odo', 'battery', 'range', 'r_bl', 'u_bl']
other_commands = ['help']

# Classes
class Car:
    """
    Attempt to represent a car with specific attributes
    and a bit of interaction with functions.
    """

    def __init__(self, make, model, year, odometer=0.0):
        """Gives the base attributes of a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = odometer
    
    def descriptive_name(self):
        """Returns a descriptive name of the car object."""
        desc_name = f'{self.year} {self.make} {self.model.title()}'
        return desc_name
    
    def read_odometer(self):
        """Print a statement showing the car's kilometers."""
        print(f'This {self.make} has {self.odometer} kilometers on it.')

    def increment_odometer(self):
        """Incrementing the odometer by with a given parameter."""
        kilometers = update_value('kilometers')
        self.odometer += kilometers
        print('Odometer successfully incremented!')

    def update_odometer(self):
        """Update the odometer reading to a specific value."""
        new_meter_value = 0
        while new_meter_value == 0:
            new_meter_value = update_value('odometer')

            # If the value for odometer is less than the current one... fraud!
            if self.odometer <= new_meter_value:
                self.odometer = new_meter_value
                print('Odometer successfuly updated!')
            else:
                new_meter_value = 0
                print('The new value must be bigger than the old one.')

class Battery:
    """
    Creates a battery object that is used by Electric cars.
    """

    def __init__(self, battery_size=75):

        self.battery_size = battery_size
        self.power_level = 100.0    # % value

    # Doesn't work properly, fix later
    def describe_battery(self):
        """Give back a descriptive info about the battery of the car."""
        print(f'This car has a {self.battery_size}-kWh battery size.')
        self.power_level -= 7
    
    def get_range(self):
        """Prints the Kilometers that the car object can travel."""
        km_range = self.battery_size * 3.5 / 0.62
        current_range = km_range * self.power_level / 100
        print(f'This car can go about {km_range:.2f}km on a full cahrge.')
        print(f'\nThe current range of the car is {current_range:.2f}km.')
        self.power_level -= 4
        
    def read_battery(self):
        """Prints the current power level of the battery."""
        print(f'The car is {self.power_level:.1f}% charged')
    
    def update_battery(self):
        """Updates the power_level of the battery. Max 100%"""
        if self.power_level == 100:
            print(f'The battery is already on a 100% charge!')
        else:
            battery_charge = 0
            while battery_charge == 0:
                battery_charge = update_value('battery charge')
                if battery_charge + self.power_level > 100:
                    overcharge = abs(battery_charge - (100 - self.power_level))
                    self.power_level = 100
                else:
                    self.power_level += battery_charge
                if overcharge:
                    print(f'Overcharge: {overcharge:.1f}%')
                    self.read_battery()
        self.power_level -= 1

class ElectricCar(Car):
    """
    Creates an object for electric cars.
    Inherits from Car class.
    """

    def __init__(self, make, model, year, odometer=0):
        """Initialize the attributes  of the parrent class."""
        super().__init__(make, model, year, odometer)
        self.battery = Battery()


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
            print(f'{cmd} is not a valid for \'{car_type}\'.')

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
