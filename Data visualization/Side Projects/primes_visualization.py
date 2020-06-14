from matplotlib import pyplot as plt

def IsPrime(num):
    """Determain if a number is prime or not"""
    if num == 2 or num == 3:
        return True
    if num < 2 or num % 2 == 0:
        return False
    if num < 9:
        return True
    if num % 3 == 0:
        return False

    max_factor = int(num**0.5) + 1
    factor = 5

    while factor < max_factor:
        if num % factor == 0:
            return False
        if num % (factor + 2) == 0:
            return False
        factor += 6
    return True

def PrimeValuePosition(max_number):
    """Visualize a plot with the prime value and its position
    relative to all numbers"""

    primes = [x for x in range(max_number + 1) if IsPrime(x)]

    # Create the figure and axes
    fig, ax = plt.subplots(figsize=(14,8), dpi=128)

    plt.style.use('seaborn')

    ax.plot(range(1, len(primes) + 1), primes, label='Primes')
    # Styling
    ax.set_title(f'Prime numbers bellow {max_number}', fontsize=24)
    ax.set_xlabel('Prime number position', fontsize=16)
    ax.set_ylabel('Prime number value', fontsize=16)

    ax.tick_params(axis='both', which='major', labelsize=12)

    #plt.axis([0, len(primes) + 1, 0, max_number])

    plt.legend()
    plt.show()

def PrimeValuePowered(max_number):
    """Visualize a plot with the prime value  powerd on 2 and its position
    relative to all numbers"""
    
    primes = [x**2 for x in range(2, max_number + 1) if IsPrime(x)]

    # Create the figure and axes
    fig, ax = plt.subplots(figsize=(14,8), dpi=128)

    ax.scatter(range(len(primes)), primes, c=primes, cmap=plt.cm.Blues,
     s=15, label='Primes')
    
    # Styling
    ax.set_title(f'Doubled Prime numbers',
     fontsize=24)
    ax.set_xlabel('Prime number', fontsize=16)
    ax.set_ylabel('Doubled prime number', fontsize=16)

    ax.tick_params(axis='both', which='major', labelsize=12)

    #plt.axis([0, max_number, 0, max_number**2])

    plt.legend()
    plt.show()

def main():
    
    while True:

        max_number = int(input('Maximum number for the primes: '))

        print('Choose a graph to show (q to quit):')
        print('1 for Prime Value Position')
        print('2 for Prime Value Powered')

        usr_inp = input('>>> ')
    
        if usr_inp == 'q':
            quit()
        
        elif usr_inp == '1':
            PrimeValuePosition(max_number)
        elif usr_inp == '2':
            PrimeValuePowered(max_number)

        else:
            print(f'Error! {usr_inp} is not a valid command.')

if __name__ == '__main__':
    main()
