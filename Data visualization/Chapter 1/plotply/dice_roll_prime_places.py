# This visualization will plot only the rolls with prime numbers
from plotly.graph_objs import Bar, Layout
from plotly import offline
from matplotlib import pyplot as plt

from die import Die
from prime import IsPrime

def PlotLy(x_values, frequencies, d_n, d_s, r_n):
    """Visualize the PlotLy type"""

    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {'title': 'Result', 'dtick':1}
    y_axis_config = {'title': 'Frequencies of result'}

    custom_layout = Layout(title=f'Rolling {d_n} D{d_s} dice {r_n} times, only plotting the prime rolls',
        xaxis=x_axis_config, yaxis=y_axis_config)

    offline.plot({'data': data, 'layout': custom_layout}, filename='prime_places_rolls.html')

def PyPlot(x_values, frequencies, d_n, d_s, r_n):
    """Visualize the PyPlot type"""
    fig, ax = plt.subplots(figsize=(14,8), dpi=128)

    ax.plot(x_values, frequencies, label='Results', linewidth=4)

    # Styling
    ax.set_title(f'Rolling {d_n} D{d_s} dice {r_n} times, only plotting the prime rolls', fontsize=24)
    ax.set_xlabel('Result', fontsize=16)
    ax.set_ylabel('Frequencies of result', fontsize=16)

    ax.tick_params(axis='both', which='major', labelsize=14)

    plt.legend()
    plt.show()

def RollDice(dice):
    """Roll all the dice in a list and return the result"""
    result = 0
    for die in dice:
        result += die.Roll()
    return result

def main():

    print('Welcome to the dice visualization!')

    dice_number = int(input('How many dice to have? '))
    dice_sides = int(input('How many sides should the dice have? '))
    roll_number = int(input('Provide a number for the amount of rolls: ')) 

    while True:

        dice = []
        for i in range(dice_number):
            dice.append(Die(dice_sides))

        # Data lists
        results = []
        frequencies = []

        min_roll = len(dice)
        max_roll = dice_number * dice_sides
        x_values = [x for x in range(min_roll, max_roll + 1)]

        # Make the rolls
        for i in range(roll_number + 1):
            if IsPrime(i):
                results.append(RollDice(dice))

        # Find the frequency of each unique roll
        for value in range(min_roll, max_roll + 1):
            frequencies.append(results.count(value))
        
        # Intro
        print('Choose the visuazlization type:', end='\n\n')
        print('Type 1 or pyplot for PyPlot visualization')
        print('Type 2 or plotly for PlotLy visualization')
        print('Type \'q\' to quit')

        usr_inp = input('>>> ').lower()

        if usr_inp == 'q':
            quit()
        
        # Visualizations
        elif usr_inp == '1' or usr_inp == 'pyplot':
            PyPlot(x_values, frequencies, dice_number, dice_sides, roll_number)
        elif usr_inp == '2' or usr_inp == 'plotly':
            PlotLy(x_values, frequencies, dice_number, dice_sides, roll_number)
        
        else:
            print(f'Error! {usr_inp} is not a valid command.\nPlease try again.')

if __name__ == '__main__':
    main()
