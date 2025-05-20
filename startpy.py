import os, pickle, random, time, sys
from enemy import Enemy
from fighting import *
from colorama import init
from termcolor import  colored

GoblinIG = Enemy('Goblin', 50, 5, 5, 10)
ZombieIG = Enemy('Zombie', 100, 10, 10, 20)
SkeletonIG = Enemy('Skeleton', 100, 10, 10, 20)
SalamanderIG = Enemy('Salamander', 100, 10, 10, 20, attacks={'Fire Breathe': 10, 'Poison Dart': 7})

weapons = {'Great Sword': 60}
armor = {'Platinum Armour': 50}

def start1(player_start=player):
    global player
    player = player_start
    while True:
        os.system('cls')
        print(colored(f'Name: {player.name}', 'green'))
        print(colored(f'Gold: {player.gold}', 'yellow'))
        print(colored(f'Potions: {player.pots}', 'blue'))
        print(colored(f'Health: {player.health}/{player.maxHealth}', 'red'))
        if player.quests_accepted != []: print(f"Current Quest: {player.quests_accepted[0]}\n")
        print('1) Fight')
        print('2) Quest')
        print('3) Store')
        print('4) Inventory')
        print('5) Explore')
        print('6) Save')
        print('7) Exit')
        option = input('-> ')
        if option == '1':
            pre_fight()
        elif option == '2':
            pre_quest()
        elif option == '3':
            store()
        elif option == '4':
            inventory()
        elif option == '5':
            explore()
        elif option == '6':
            os.system('cls')
            with open('savefile.txt', 'wb') as f:
                pickle.dump(player, f)
                print('\nGame Has Been Saved\n')
            input(' ')
            start1()
        elif option == '7':
            sys.exit()

def inventory():
    while True:
        os.system('cls')
        print('What do you want to do?')
        print(colored('1) Equip Weapon/Armour', 'grey'))
        print(colored(f'2) Health Potion - {player.pots}', 'red'))
        print('b) Go Back')
        option = input('>>> ')
        if option == '1':
            equip()
        elif option == '2':
            drink_potion(player)
        elif option == 'b':
            return

def equip():
    while True:
        os.system('cls')
        print('What do you want to equip?')
        for weapon in player.weapon:
            print(weapon)
        for armour in player.armor:
            print(armour)
        print('b) Go Back')
        option = input('>>> ')

        if option == player.current_weapon:
            print(colored('You have already equipped this weapon', 'red'))
            input(' ')
        elif option == player.current_armor:
            print(colored('You have already equipped this armour', 'red'))
            input(' ')
        elif option in player.weapon:
            player.current_weapon = option
            print(colored(f'You have equipped {option}', 'green'))
            input(' ')
        elif option in player.armor:
            player.current_armor = option
            print(colored(f'You have equipped {option}', 'green'))
            input(' ')
        elif option == 'b':
            return
        else:
            print(colored(f"You don't have {option} in your inventory", 'green'))

def pre_fight():
    global enemy
    enemy_random = random.choices([1, 2, 3], weights=[3, 2, 1], k=1)
    if enemy_random[0] == 1:
        enemy = GoblinIG
    elif enemy_random[0] == 2:
        enemy = ZombieIG
    elif enemy_random[0] == 3:
        enemy = SkeletonIG
    fight(player=player, enemy=enemy)

def store():
    while True:
        os.system('cls')
        print('Welcome to the shop!')
        print('\nWhat would you like to buy?\n')
        print('Great Sword: 60')
        print('Platinum Armour: 50')
        print(colored('Health Potion: 5', 'red'))
        print('back) Go Back')
        option = input('-> ')
        if option in weapons:
            if player.gold >= weapons[option]:
                os.system('cls')
                player.gold -= weapons[option]
                player.weapon.append(option)
                print(colored(f'You have bought {option}', 'green'))
                input(' ')
            else:
                os.system('cls')
                print(colored("You don't have enough gold!", 'red'))
                input(' ')
        elif option in armor:
            if player.gold >= armor[option]:
                os.system('cls')
                player.gold -= armor[option]
                player.armor.append(option)
                print(colored(f'You have bought {option}', 'green'))
                input(' ')
            else:
                os.system('cls')
                print(colored("You don't have enough gold!", 'red'))
                input(' ')
        elif option == 'Health Potion':
            if player.gold >= 5:
                player.gold -= 5
                player.pots += 1
                os.system('cls')
                print(colored('You successfully brought a health potion!', 'green'), f'You have {player.pots} potions now')
                input(' ')
        elif option == 'back':
            start1()
        else:
            os.system('cls')
            print(colored('That item does not exist!', 'red'))
            option = input(' ')
            store()

def pre_quest(questChoice=None):
    while True:
        if questChoice == None:
            quests = ['Please find my 5 naughty children', 'Can you bring the lost diamond coin', 'Follow the purple marks on the rocks, they will lead you to a secret', 'The griffin there is not keeping the other village happy, someone has to do something.', 'Help me build the bridge please!']
            questChoice = random.choice(quests)
        os.system('cls')
        print(f'NPC: {questChoice}')
        option = input('-> ')
        if option.lower() == 'y' or option.lower() == 'yes' or option.lower() == 'yup' or (option.lower() == 'ok') or (option.lower() == 'okay'):
            player.quests_accepted.append(questChoice)
            os.system('cls')
            print(colored(f'You have accepted {questChoice}', 'green'))
            input(' ')
        elif option.lower() == 'n' or option.lower() == 'no' or option.lower() == 'nope':
            return

def explore():
    exploreOptions = ['You see weird colors on the rocks', 'The sky is a unique color today!', 'The trees are there as far as I can see', 'The great hall looks great as always']
    weights = [1.3, random.randrange(0.7, 1.2), random.randrange(0.5, 1.4), 1]
    if not exploreOptions[0] in player.quests_accepted or not exploreOptions[0] in player.quests_completed:
        exploreWhat = random.choices(exploreOptions, weights=weights, k=1)[0]
    else: exploreWhat = random.choice(exploreOptions[1:])
    print(exploreWhat)
    if exploreWhat == 'You see weird colors on the rocks':
        while True:
            print('You approach the rocks wearily:')
            print('1) Inspect')
            print('2) Investigate')
            print('b) Go Back')
            option = input('-> ')
            match option:
                case '1':
                    while True:
                        print('1) Touch')
                        print('2) Taste')
                        print('3) Smell')
                        option = input('> ')
                        match option:
                            case '1':
                                print('You touch the rock and nothing happens, you dust off the red colour from your hands.')
                                print("Or was it green? The colors on the rock don't stay constant!")
                            case '2':
                                print("You spit out the color mixed with so many minerals that it shouldn't be good for you.")
                                print("There is a lingering taste like mud.")
                            case '3':
                                print('The smell is heavenly and takes you back to your good old days as a weary barn farmer.')
                                print('Was it a barn farmer or a tavern owner? or was your father in the adventurers\' guild?')
                                print('You sit there awhile, thinking about your past, you memories, or rather... lack thereof.')
                            case _:
                                break
                case '2':
                    print("You investigate the rock and ask people about it. People say they don't know but one of them says that he knows!")
                    pre_quest('Follow the purple marks on the rocks, they will lead you to a secret')
                case _:
                    break
    else:
        print('1) Keep Exploring')
        print('2) Go back')
        option = input('-> ')
        if option == '1':
            explore()
        option = input(' ')
