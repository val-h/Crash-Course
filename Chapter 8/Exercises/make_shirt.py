shirt_size = input('Size of shirt: ').lower()
shirt_message = input('Message to be printed on the shirt: ')

def shirt_design(shirt_message, shirt_size='m'):
    """A simple way to design a shirt using a message and size for it."""
    print(f'Designing a shirt sized {shirt_size.title()} with a message {shirt_message} ...')

if shirt_size:
    shirt_design(shirt_message, shirt_size)
else:
    shirt_design(shirt_message)
