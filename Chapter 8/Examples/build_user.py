def build_user(first, last, **user_info):
    """Simple way of building a user for a website."""
    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info

f_name, l_name = input('First and last name (Seperated with space): ').split()

print(build_user(f_name, l_name, location='princeton', filed='physics'))
