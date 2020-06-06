# Module for quick testing of plots and functions
#
# Every new thing i try will be put in a seperate function,
# just so i can keep the stuff i wrote

from matplotlib import pyplot as plt

def square_cubic_plot():
    a = [x for x in range(25)]  # don't go overboard with this value,
    # it messes up the color and size variables :D

    fig, ax = plt.subplots()

    # Ploting the data using a loop, not using numpy
    for i in a:
        color = i * 0.03 + 0.1
        size = i * 0.25 + 50 
        
        # Looping through the whole list and plotting seperatly the values
        ax.scatter(a[i], a[i], s=size, c=(color, 0, 0), label='normal') # Normal
        ax.scatter(a[i], a[i]**2, s=size, c=(0, color, 0), label='square') # Square
        ax.scatter(a[i], a[i]**3, s=size, c=(0, 0, color), label='cubic') # Cubic

    # Styling
    ax.set_title('Square and Cubics', fontsize=26)
    ax.set_xlabel('Numbers', fontsize=16)
    ax.set_ylabel('Result', fontsize=16)

    # Okay... the legend doesn't work as i expected :'D
    #plt.legend()

    plt.show()

square_cubic_plot()
