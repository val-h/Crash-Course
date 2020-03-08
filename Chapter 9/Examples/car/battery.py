from garage import update_value

"""A class that will represent a battery for an Electric car."""

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
