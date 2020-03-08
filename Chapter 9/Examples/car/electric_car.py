from car import Car
from battery import Battery

"""A class representin an Electri car."""

class ElectricCar(Car):
    """
    Creates an object for electric cars.
    Inherits from Car class.
    """

    def __init__(self, make, model, year, odometer=0):
        """Initialize the attributes  of the parrent class."""
        super().__init__(make, model, year, odometer)
        self.battery = Battery()
