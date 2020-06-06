import numpy as np # first use of np, Yay!
from matplotlib import pyplot as plt

a = np.arange(0, 5, 0.2) # and i don't know what it does :D

plt.style.use('seaborn') # I quite like this style

fig, ax = plt.subplots() # OO version, explicitly create the figure and axes

# Plots the diferent values and sets their unique label for the legend
ax.plot(a, a, 'r--', label='normal')
ax.plot(a, a**2, 'bs', label='square')
ax.plot(a, a**3, 'g^', label='cubic')

# Set chart title and axes labels
ax.set_title('Square and Cubic numbers', fontsize=24)
ax.set_xlabel('Numbers', fontsize=16)
ax.set_ylabel('Result', fontsize=16)

# Set the size of both major tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([-0.2, 5.2, -5, 120]) # Configures the min and max of both axes, x and y

ax.legend() # Shows the legend

plt.show() # Show the figure
