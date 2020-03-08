"""Essential functions for the program."""

def update_value(value_name):
    """
    Asks the user for a positive value until it gets one.
    Requires a string parameter for the input message in format:
            Value for {value_name}: 
    """
    while True:
        try:
            temp_value = float(input(f'Value for {value_name}: '))
        except:
            print('Please write a number...')
        else:
            if temp_value <= 0:
                print('Please write a positive number.....')
                continue
            else:
                break
    return temp_value 
