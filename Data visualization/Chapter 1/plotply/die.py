from random import randint

class Die:
    """A class to represent diferent types of dice"""

    def __init__(self, sides=6):

        self.sides = sides
    
    def Roll(self):
        """Mothod for rolling the die"""
        return randint(1, self.sides)
        