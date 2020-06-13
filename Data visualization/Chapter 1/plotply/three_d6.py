from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create 3 different D6 dices
d_1 = Die()
d_2 = Die()
d_3 = Die()
dice_list = [d_1, d_2, d_3]

# Other variables
results = []
frequencies = []

number_of_rolls = 5000

min_roll_number = len(dice_list)
max_roll_number = min_roll_number * d_1.sides

# Create the rolls
for roll in range(number_of_rolls):
    results.append(d_1.Roll() + d_2.Roll() + d_3.Roll())

# Add the frequencies
for value in range(min_roll_number, max_roll_number + 1):
    frequencies.append(results.count(value))

# Visualize and style the hystogram

x_values = [x for x in range(min_roll_number, max_roll_number + 1)]
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Results', 'dtick':1}
y_axis_config = {'title': 'Frequency of results'}

custom_layout = Layout(title=f'Results of rolling {min_roll_number} D6 dices {number_of_rolls} times',
    xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': custom_layout}, filename='three_d6_dices.html')
