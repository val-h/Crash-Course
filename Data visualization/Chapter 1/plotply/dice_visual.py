from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two dice
die_1 = Die()
die_2 = Die(10)
roll_count = 50000
max_values_sides = die_1.sides + die_2.sides

results = []
frequencies = []

# Roll the dice 'roll_count' times and add the sum to the results
for i in range(roll_count):
    results.append(die_1.Roll() + die_2.Roll())

# Calculate the frequencies of the rolled dice
for value in range(2, max_values_sides + 1):
    # Count the total results of 'value' in the list and add them to a list
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the data
x_values = [x for x in range(2, max_values_sides + 1)]
data = [Bar(x=x_values, y=frequencies)]

# Dictionaries for the description of the layout, kwargs for xaxis and yaxis
x_axis_config = {'title': 'Results', 'dtick':1}
y_axis_config = {'title': 'Frequency of Results'}

# Creating the layout using 'title' and passing the dictionaries 
my_layout = Layout(title='Frequency results of D6 and D 10 dice rolled 50000 times',
    xaxis=x_axis_config, yaxis=y_axis_config)

# Creating the html file containing the plot, using the generated graph
# and custom layout that is defind, 'filename' is self-explanatory
offline.plot({'data': data, 'layout':my_layout}, filename='d6_d10_dices.html')
