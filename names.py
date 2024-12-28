import random

def name_menu():
    """
    Continuously generates a random name and asks the user if they want to 
    keep it. Returns the name if the user confirms with 'y'.
    """
    while True:
        name_chosen = name_choice()
        print(f'Do you want {name_chosen} to be your name?')
        print('y/n')
        option = input('')
        if option == 'y':
            return name_chosen

def name_choice():
    with open('rpg_names.txt', 'r') as f:
        name = [x.strip() for x in f.read().split(',')]
    name = random.choice(name)
    return name
