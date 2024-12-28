import sys, os, random, pickle, names
from player import Player
from enemy import Enemy
from fighting import *

# TODO: Implement a magic system with potions for buffs, debuffs, and throwable effects

weapons = {'Great Sword': 60}
armor = {'Platinum Armour': 50}

GoblinIG = Enemy('Goblin', 50, 5, 5, 10)
ZombieIG = Enemy('Zombie', 100, 10, 10, 20)
SkeletonIG = Enemy('Skeleton', 100, 10, 10, 20)
SalamanderIG = Enemy('Salamander', 100, 10, 10, 20, attacks={'Fire Breathe': 10, 'Poison Dart': 7})

def main():
    global PlayerIG
    while True:
        os.system('cls')
        print('\nWelcome to Fantasy RPG\n')
        print('1) Start')
        print('2) Load')
        print('3) Exit')
        option = input('-> ')
        if option == '1':
            start()
            start1()
        elif option == '2':
            if os.path.exists('savefile.txt') == True:
                os.system('cls')
                with open('savefile.txt', 'rb') as f:
                    PlayerIG = pickle.load(f)
                print('Loaded Save State')
                input(' ')
                start1()
            else:
                print('You have no save file for this game!')
                input(' ')
                main()
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

def start1():
    while True:
        os.system('cls')
        print(f'Name: {PlayerIG.name}')
        print(f'Gold: {PlayerIG.gold}')
        print(f'Potions: {PlayerIG.pots}')
        print(f'Health: {PlayerIG.health}/{PlayerIG.maxHealth}')
        if PlayerIG.quests_accepted != []: print(f"Current Quest: {PlayerIG.quests_accepted[0]}")
        print('\n')
        print('1) Fight')
        print('2) Quest')
        print('3) Store')
        print('4) Save')
        print('5) Exit')
        print('6) Inventory')
        print('7) Explore')
        option = input('-> ')
        if option == '1':
            pre_fight()
        elif option == '2':
            pre_quest()
        elif option == '3':
            store()
        elif option == '4':
            os.system('cls')
            with open('savefile.txt', 'wb') as f:
                pickle.dump(PlayerIG, f)
                print('\nGame Has Been Saved\n')
            input(' ')
            start1()
        elif option == '5':
            sys.exit()
        elif option == '6':
            inventory()
        elif option == '7':
            explore()

def inventory():
    while True:
        os.system('cls')
        print('What do you want to do?')
        print('1) Equip Weapon/Armour')
        print(f'2) Health Potion - {PlayerIG.pots}')
        print('b) Go Back')
        option = input('>>> ')
        if option == '1':
            equip()
        elif option == '2':
            drink_potion(PlayerIG)
        elif option == 'b':
            return

def equip():
    while True:
        os.system('cls')
        print('What do you want to equip?')
        for weapon in PlayerIG.weapon:
            print(weapon)
        for armour in PlayerIG.armor:
            print(armour)
        print('b) Go Back')
        option = input('>>> ')

        if option == PlayerIG.current_weapon:
            print('You have already equipped this weapon')
            input(' ')
        elif option == PlayerIG.current_armor:
            print('You have already equipped this armour')
            input(' ')
        elif option in PlayerIG.weapon:
            PlayerIG.current_weapon = option
            print(f'You have equipped {option}')
            input(' ')
        elif option in PlayerIG.armor:
            PlayerIG.current_armor = option
            print(f'You have equipped {option}')
            input(' ')
        elif option == 'b':
            return
        else:
            print(f"You don't have {option} in your inventory")

def pre_fight():
    global enemy
    enemy_random = random.choices([1, 2, 3], weights=[3, 2, 1], k=1)
    if enemy_random[0] == 1:
        enemy = GoblinIG
    elif enemy_random[0] == 2:
        enemy = ZombieIG
    elif enemy_random[0] == 3:
        enemy = SkeletonIG
    fight(player=PlayerIG, enemy=enemy)

def store():
    while True:
        os.system('cls')
        print('Welcome to the shop!')
        print('\nWhat would you like to buy?\n')
        print('Great Sword: 60')
        print('Platinum Armour: 50')
        print('Health Potion: 5')
        print('back) Go Back')
        option = input('-> ')
        if option in weapons:
            if PlayerIG.gold >= weapons[option]:
                os.system('cls')
                PlayerIG.gold -= weapons[option]
                PlayerIG.weapon.append(option)
                print(f'You have bought {option}')
                input(' ')
            else:
                os.system('cls')
                print("You don't have enough gold!")
                input(' ')
        elif option in armor:
            if PlayerIG.gold >= armor[option]:
                os.system('cls')
                PlayerIG.gold -= armor[option]
                PlayerIG.armor.append(option)
                print(f'You have bought {option}')
                input(' ')
            else:
                os.system('cls')
                print("You don't have enough gold!")
                input(' ')
        elif option == 'Health Potion':
            if PlayerIG.gold >= 5:
                PlayerIG.gold -= 5
                PlayerIG.pots += 1
                os.system('cls')
                print(f'You successfully brought a health potion! You have {PlayerIG.pots} potions now')
                input(' ')
        elif option == 'back':
            start1()
        else:
            os.system('cls')
            print('That item does not exist!')
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
            PlayerIG.quests_accepted.append(questChoice)
            os.system('cls')
            print(f'You have accepted {questChoice}')
            input(' ')
        elif option.lower() == 'n' or option.lower() == 'no' or option.lower() == 'nope':
            return

def explore():
    exploreOptions = ['You see weird colors on the rocks', 'The sky is a unique color today!', 'The trees are there as far as I can see', 'The great hall looks great as always']
    weights = [1.3, random.randrange(0.7, 1.2), random.randrange(0.5, 1.4), 1]
    if not exploreOptions[0] in PlayerIG.quests_accepted or not exploreOptions[0] in PlayerIG.quests_completed:
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

if __name__ == "__main__": 
    main()