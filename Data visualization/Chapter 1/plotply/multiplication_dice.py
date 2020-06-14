from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die()
die_2 = Die()

max_roll = 12
min_roll = 2

roll_number = 5000

results = []
frequencies = []

for i in range(roll_number):
    results.append(die_1.Roll() * die_2.Roll())

for value in range(6**2):
    frequencies.append(results.count(results[value]))

# Visualize the data

x_values = [x * y for x in range(1, die_1.sides +1 ) for y in range(1, die_2.sides + 1)]
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Multiples of the 2 dice', 'dtick':1}
y_axis_config = {'title': 'Frequencies of the multiples'}


custom_layout = Layout(title='Frequency of multiples of 2 D6', xaxis=x_axis_config,
    yaxis=y_axis_config)

offline.plot({'data': data, 'layout': custom_layout}, filename='multiple_of_d6_dice.html')
