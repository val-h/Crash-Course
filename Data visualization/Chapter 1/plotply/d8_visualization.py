from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create the two d8 dices
die_1 = Die(8)
die_2 = Die(8)
results = []
frequencies = []

# Trying a big number
number_of_rolls = 500000

min_sides_value = 2
max_sides_value = die_1.sides + die_2.sides

# Loop through the rolls
for roll in range(number_of_rolls):
    results.append(die_1.Roll() + die_2.Roll())

# Calculating the frequencies
for value in range(min_sides_value, max_sides_value + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Create the hystogram and make a layout for it

x_values = [x for x in range( min_sides_value, max_sides_value + 1)]
data = [Bar(x=x_values, y=frequencies)]

# It would be nice to see the documentation for more styling information
x_axis_config = {'title': 'Results', 'dtick':1}
y_axis_config = {'title': 'Frequency of the results'}

custom_layout = Layout(title='Results of rolling two D8 dices', 
    xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': custom_layout}, filename='two_d8_dices.html')
