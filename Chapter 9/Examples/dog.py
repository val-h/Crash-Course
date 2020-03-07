from random import randint

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age, **kwargs):

        self.name = name
        self.age = age
        self.others = kwargs
    
    def attributes(self):
        print(f'My dog {self.name} is {self.age} years-old.')
        if self.others:
            print(f'Extra information about {self.name}:')
            for extra_atrb in self.others:
                print(f'\t{extra_atrb} - {self.others[extra_atrb]}')
    
    def sit(self):
        """Gives the dog a command to sit."""
        print(f'{self.name} is now sitting.')
    
    def roll(self):
        """Gives the dog a command to roll over."""
        print(f'{self.name} rolled over!')
    
    def give_paw(self):
        """Depending on the mood of the dog it might give you a paw : / """
        mood = randint(0, 10)
        if mood < 5:
            print(f'{self.name} just gave you his paw!')
        else:
            print(f'{self.name} doesn\'t seem to be in a mood for games : /')
        pass
        
    
my_dog = Dog('Cezar', 9, breed='husky', eye_color='blue', fur_color='white')

while True:
    cmd = input('/> ')
    if cmd == 'q':
        print('Exiting program...')
        break

    if cmd == 'info':
        my_dog.attributes()
    elif cmd == 'sit':
        my_dog.sit()
    elif cmd == 'roll':
        my_dog.roll()
    elif cmd == 'paw':
        my_dog.give_paw()
    else:
        print(f'Error! {cmd} is not a valid command.')
