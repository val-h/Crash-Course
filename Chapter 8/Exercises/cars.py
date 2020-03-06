def car_builder(make, model, generation, **kwargs):
    """Extended way of building a car with additional information."""
    car = [make, model, generation]
    for kwarg in kwargs:
        car.append(f'{kwarg} - {kwargs[kwarg]}')
    return car

make, model, generation = input('Make, Model and Generation of a car (Seperated with a \'-\'): ').split('-')

new_car = car_builder(make, model, generation, sportscar=True)
print(new_car)
