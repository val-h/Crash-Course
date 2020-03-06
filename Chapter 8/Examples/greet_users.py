def greet_users(list_with_names):
    """Great each user individually."""
    for user in list_with_names:
        print(f'Hello, {user.title()}!')

names = input('Enter user names seperated with blank space: ').split()
greet_users(names)
