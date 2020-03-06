pizza_size = input('Size of the pizza you want: ')

def make_pizza(size, *toppings):    # *toppings takes an arbirtrary number of arguments
    """Simple way of describing a pizza with toppings."""
    print(f'Makeing a {size}cm. sized pizza with {len(toppings)} toppings.')
    for topping in toppings:
        print(f'- {topping}')

make_pizza(pizza_size, 'pepperoni', 'corn', 'spicy peppers', 'extra cheese')
