from essentials import update_value

"""A class that can be used to represent a car."""

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
