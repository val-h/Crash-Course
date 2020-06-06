from random import choice

class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, num_points=5000):
        """
        Attributes required for the walk: 'steps' variable for the count
        and 2 lists to store the x, y coordinates of each step
        """
        self.num_points = num_points

        # All walks start at (0, 0)
        self.x = [0]
        self.y = [0]
    
    def fill_walk(self):
        """Calculate all the points in the walk"""
        # Set the maximum movement
        while len(self.x) < self.num_points:
            # x steps calculation
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            # y steps calculation
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # reject steps that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # new position
            x = self.x[-1] + x_step
            y = self.y[-1] + y_step

            # add the steps to their lists
            self.x.append(x)
            self.y.append(y)
