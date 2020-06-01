import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')

# Figure
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=(0, 0.8, 0),s=10) # Finally adding color

# c='red' / c=(0, 0, 1) both of these work, eigther pass a tuple with value
# from 0 to 1 or a string with the name of the color in lower case

# Styling
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([0, 1100, 0, 1200000])  # y_max does not show correctly

plt.show()
