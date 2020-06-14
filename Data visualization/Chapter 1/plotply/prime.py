def IsPrime(num):
    """A function to determine if a number is prime or not"""
    
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

    # Run a loop with all the possible factors
    while factor < max_factor:
        if num % factor == 0:
            return False
        if num % (factor + 2) == 0:
            return False
        factor += 6

    # If all the possible factors fail, the number is a prime
    return True

def main():
    for i in range(1000):
        if IsPrime(i):
            print(i)

if __name__ == '__main__':
    main()
    