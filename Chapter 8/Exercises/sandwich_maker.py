bread = input('Type of bread: ')

def sandwich_builder(bread, *ingredients):
    """Simply describing a sandwich that a customer wants."""
    print(f'\nYou want a sandwich with {bread} bread and {len(ingredients)} ingredients in it.')
    for ingredient in ingredients:
        print(f'Adding {ingredient} in the sandwich.')
    print('\nDone! Your sandwich is ready.')

sandwich_builder(bread, 'Tomatoes', 'Cucumbers', 'Salami', 'Cheese', 'Spicy Peppers', 'Olives')
