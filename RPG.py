import sys, os, pickle, names
from player import Player
from rich import traceback
from startpy import *

#** INITIALIZATION **#
traceback.install()
init()

# TODO: Implement a magic system with potions for buffs, debuffs, and throwable effects

def main():
    global PlayerIG
    while True:
        os.system('cls')
        print(colored('\nWelcome to Fantasy RPG\n', 'light_magenta'))
        print('1) Start')
        print('2) Load')
        print('3) Exit')
        option = input('-> ')
        if option == '1':
            start()
            start1(PlayerIG)
        elif option == '2':
            if os.path.exists('savefile.txt') == True:
                os.system('cls')
                with open('savefile.txt', 'rb') as f:
                    PlayerIG = pickle.load(f)
                print('Loaded Save State')
                input(' ')
                start1(PlayerIG)
            else:
                print('You have no save file for this game!')
                input(' ')
        elif option == '3':
            sys.exit()

def start():
    global PlayerIG
    os.system('cls')
    print('Hello, what is your name?')
    print('1) R to randomize')
    option = input('-> ')
    if option.lower() != 'r':
        name = option
        PlayerIG = Player(name)
    else:
        name = names.name_menu()
        PlayerIG = Player(name)

if __name__ == "__main__": 
    main()