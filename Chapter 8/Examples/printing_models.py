def model_printing(waiting_models, printed_models):
    """
    Simulate printing each design until none are left.
    Move the printed design in another list.
    """

    while waiting_models:
        current_model = waiting_models.pop(0)
        print(f'\nPrinting {current_model.title()}...')
        printed_models.append(current_model)
        print(f'{current_model.title()} has been printed!')

# Receiving a sting of objects seperated with '-', converted to a list
designs_to_be_printed = input('Enter the designs you wish to print (Seperated only with \'-\'): ').split('-')
finished_designs = []

model_printing(designs_to_be_printed[:], finished_designs)

print('\nOriginal designs - ', designs_to_be_printed)
print('\nList with finished designs - ', finished_designs)
