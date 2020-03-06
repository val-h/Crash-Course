pet_type = input('Type of pet: ')
pet_name = input('Name of your pet: ')

def describe_pet(pet_name, pet_type='dog'):
    """A simple way to describe a pet."""
    print(f'Your {pet_type}\'s name is {pet_name.title()}.')

if pet_type:
    describe_pet(pet_name, pet_type)
else:
    describe_pet(pet_name)
