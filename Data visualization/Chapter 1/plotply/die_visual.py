from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

results = []
die = Die()

for i in range(1000):
    result = die.Roll()
    results.append(result)

frequencies = []
for value in range(1, die.sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the data

x_values = [x for x in range(1, die.sides + 1)]
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Results'}
y_axis_config = {'title': 'Frequencies'}

my_layout = Layout(title='Results of rolling D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
