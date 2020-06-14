from matplotlib import pyplot as plt

from random_walk import RandomWalk

# Create a random walk

def visualize_walk(walk_steps):
    """Vizualize the walk"""

    # Generate the random walk pattern
    rw = RandomWalk(walk_steps)
    rw.fill_walk()

    # creating the figure and scattering the steps on the plot
    fig, ax = plt.subplots(figsize=(14, 8), dpi=128)
    
    ordered_steps = range(walk_steps)
    ax.scatter(rw.x, rw.y, s=5, c=ordered_steps, cmap=plt.cm.Blues,
     edgecolors='none', label='Steps(lighter - beginning, darker-end')
    
    #Emphasize the first and last point
    ax.scatter(0, 0, c='green', s=50, edgecolors='none', label='Start')
    ax.scatter(rw.x[-1], rw.y[-1], c='red', s=50, edgecolors='none',
     label='Finish')

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    ax.set_title('Random Walk Generator', fontsize=26)
    
    plt.legend()
    plt.show()

# Loop for the program to manipulate the walk and restart it
while True:
    print(' - Random Walk Generator - ')
    generate_walk = input('Do you want to plot a pattern( y/n )? - ')
    if generate_walk == 'y':
        try:
            walk_steps = int(input('How many steps to take? - '))            
        except:
            print('Invalid input! Please enter a valid integer.')
            continue
        else:
            print(f'Generating a walk with {walk_steps} steps...')
        
        visualize_walk(walk_steps)
    elif generate_walk == 'n':
        print('Quiting program...')
        break
