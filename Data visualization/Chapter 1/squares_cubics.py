# Try it yourself exercise.
# Create a plot of Cubics(will also add squares) and add a color map to it

from matplotlib import pyplot as plt


def square_cubic_plot():
    """Creates a plot with the normal, squared and cubic values
    of the first n numbers"""

    n = int(input('Enter a number to plot for: '))

    normal_values = range(n)
    square_values = [x**2 for x in normal_values]
    cubic_values = [x**3 for x in normal_values]

    plt.style.use('seaborn')
    
    fig, ax = plt.subplots()

    ax.scatter(normal_values, normal_values, s=25, c=normal_values, cmap=plt.cm.Blues, label='normal')
    ax.scatter(normal_values, square_values, s=25, c=square_values, cmap=plt.cm.RdYlGn, label='square')
    ax.scatter(normal_values, cubic_values, s=25, c=cubic_values, cmap=plt.cm.YlOrRd, label='cubic')

    # Styling
    ax.set_title('Squares and Cubics', fontsize=26)
    ax.set_xlabel('Numbers', fontsize=16)
    ax.set_ylabel('Result', fontsize=16)

    ax.tick_params(axis='both', which='major', labelsize=14)

    plt.legend()

    plt.show()
    # plt.savefig('squares_cubics_plot.png') could also be used to save it 
    # rather than display it

square_cubic_plot()
