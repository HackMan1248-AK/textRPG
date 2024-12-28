import sys
import os
import random
import pickle
import names
from player import Player
from enemy import Enemy
weapons = {'Great Sword': 60}
armor = {'Platinum Armour': 50}

GoblinIG = Enemy('Goblin', 50, 5, 5, 10)
ZombieIG = Enemy('Zombie', 100, 10, 10, 20)
SkeletonIG = Enemy('Skeleton', 100, 10, 10, 20)
SalamanderIG = Enemy('Salamander', 100, 10, 10, 20, attacks={'Fire Breathe': 10, 'Poison Dart': 7})

def main():
    global PlayerIG
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
            option = input(' ')
            start1()
        else:
            print('You have no save file for this game!')
            option = input(' ')
            main()
    elif option == '3':
        sys.exit()
    else:
        main()

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
        name = nema()
        PlayerIG = Player(name)

def start1():
    os.system('cls')
    print('Name: %s' % PlayerIG.name)
    print('Gold: %i' % PlayerIG.gold)
    print('Potions: %i' % PlayerIG.pots)
    print('Health: %i/%i \n' % (PlayerIG.health, PlayerIG.maxHealth))
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
        option = input(' ')
        start1()
    elif option == '5':
        sys.exit()
    elif option == '6':
        inventory()
    elif option == '7':
        explore()
    else:
        start1()

def inventory():
    os.system('cls')
    print('What do you want to do?')
    print('1) Equip Weapon/Armour')
    print('2) Health Potion - %i' % PlayerIG.pots)
    print('b) Go Back')
    option = input('>>> ')
    if option == '1':
        equip()
    elif option == '2':
        drink_potion(fighting=False)
    elif option == 'b':
        start1()
    else:
        inventory()

def equip():
    os.system('cls')
    print('What do you want to equip?')
    for weapon in PlayerIG.weap:
        print(weapon)
    for armour in PlayerIG.armor:
        print(armour)
    print('b) Go Back')
    option = input('>>> ')
    if option == PlayerIG.curweap:
        print('You have already equipped this weapon')
        option = input(' ')
        equip()
    elif option == PlayerIG.curarmor:
        print('You have already equipped this armour')
        option = input(' ')
        equip()
    elif option == 'b':
        inventory()
    elif option in PlayerIG.weap:
        PlayerIG.currweapon= option
        print('You have equipped %s' % option)
        option = input(' ')
        equip()
    elif option in PlayerIG.armor:
        PlayerIG.currarmor = option
        print('You have equipped %s' % option)
        option = input(' ')
        equip()
    else:
        print("You don't have %s in your inventory" % option)

def pre_fight():
    global enemy
    enemy_random = random.choices([1, 2, 3], weights=[3, 2, 1], k=1)
    if enemy_random == 1:
        enemy = GoblinIG
    elif enemy_random == 2:
        enemy = ZombieIG
    else:
        enemy = SkeletonIG
    fight()

def fight():
    os.system('cls')
    print('%s \t\t vs \t\t %s' % (PlayerIG.name, enemy.name))
    print("%s's Health: %d/%d \t %s's Health: %i/%i" % (PlayerIG.name, PlayerIG.health, PlayerIG.maxHealth, enemy.name, enemy.health, enemy.maxHealth))
    print('Potions: %s' % PlayerIG.pots)
    print('1) Attack')
    print('2) Drink Potion')
    print('3) Run')
    option = input(' ')
    if option == '1':
        attack()
    elif option == '2':
        drink_potion()
    elif option == '3':
        run()
    else:
        fight()

def attack():
    os.system('cls')
    PAttack = random.randint(PlayerIG.attack // 2, PlayerIG.attack)
    EAttack = random.randint(enemy.attack // 2, enemy.attack)
    if PAttack == PlayerIG.attack // 2:
        print('You miss')
    else:
        enemy.health -= PAttack
        print('You deal %i damage!' % PAttack)
    option = input(' ')
    if enemy.health <= 0:
        win()
    os.system('cls')
    if EAttack == enemy.attack // 2:
        print('The %s missed' % enemy.name)
    else:
        dd = EAttack * 2 - PlayerIG.defense // 2
        if dd >= 0:
            PlayerIG.health -= EAttack * 2 - PlayerIG.defense // 2
        print('The %s deals %i damage!' % (enemy.name, EAttack * 2 - PlayerIG.defense // 2))
    option = input(' ')
    if PlayerIG.health <= 0:
        dead()
    else:
        fight()

def drink_potion(fighting=True):
    os.system('cls')
    if PlayerIG.pots == 0:
        print("You don't have any potions!")
    else:
        PlayerIG.health += 50
        PlayerIG.pots -= 1
        if PlayerIG.health > PlayerIG.maxHealth:
            PlayerIG.health = PlayerIG.maxHealth
        print('You drank a potion! You now have %i potions.' % PlayerIG.pots)
    option = input(' ')
    if fighting == True:
        fight()
    else:
        start1()

def run():
    os.system('cls')
    runnum = random.randint(1, 3)
    if runnum == 1:
        print('You have succesfully ran away!')
        option = input(' ')
        start1()
    else:
        print('You failed to get away!')
        option = input(' ')
        os.system('cls')
        EAttack = random.randint(enemy.attack // 2, enemy.attack)
        if EAttack == enemy.attack // 2:
            print('The %s missed' % enemy.name)
        else:
            PlayerIG.health -= EAttack * 6 - PlayerIG.defense
            print('The %s deals %i damage!' % (enemy.name, EAttack * 6 - PlayerIG.defense))
        option = input(' ')
        if PlayerIG.health <= 0:
            dead()
        else:
            fight()

def win():
    os.system('cls')
    enemy.health = enemy.maxHealth
    PlayerIG.gold += enemy.goldgain
    print('You have defeated the %s' % enemy.name)
    print('%s dropped %i gold!' % (enemy.name, enemy.goldgain))
    potionPossibility = random.randint(1, 2)
    if potionPossibility == '1':
        print('%s also dropped a potion! You now have %i potions.' % (enemy.name, PlayerIG.pots))
    option = input(' ')
    start1()

def dead():
    os.system('cls')
    print('You died a heroic death!')
    option = input(' ')
    start1()

def store():
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
            PlayerIG.weaponappend(option)
            print('You have bought %s' % option)
            option = input(' ')
            store()
        else:
            os.system('cls')
            print("You don't have enough gold!")
            option = input(' ')
            store()
    elif option in armor:
        if PlayerIG.gold >= armor[option]:
            os.system('cls')
            PlayerIG.gold -= armor[option]
            PlayerIG.armor.append(option)
            print('You have bought %s' % option)
            option = input(' ')
            store()
        else:
            os.system('cls')
            print("You don't have enough gold!")
            option = input(' ')
            store()
    elif option == 'Health Potion':
        if PlayerIG.gold >= 5:
            PlayerIG.gold -= 5
            PlayerIG.pots += 1
            os.system('cls')
            print('You succesfully brought a health potion! You have %i potions now' % PlayerIG.pots)
            option = input(' ')
            store()
        else:
            os.system('cls')
            print("You don't have enough money")
    elif option == 'back':
        start1()
    else:
        os.system('cls')
        print('That item does not exist!')
        option = input(' ')
        store()

def name_choice():
    name = random.choice(names.name)
    return name

def nema():
    name = name_choice()
    print('Do you want %s to be your name?' % name)
    print('y/n')
    option = input('')
    if option == 'y':
        return name
    if option == 'n':
        nema()

def pre_quest(quests=None):
    if quests == None:
        quests = ['Please find my 5 naughty children', 'Can you bring the lost diamond coin', 'Follow the purple marks on the rocks, they will lead you to a secret', 'The griffin there is not keeping the other village happy, someone has to do something.', 'Help me build the bridge please!']
        quest_num = random.choice(quests)
    os.system('cls')
    print('NPC: ' + quest_num)
    option = input('-> ')
    if option.lower() == 'y' or option.lower() == 'yes' or option.lower() == 'yup' or (option.lower() == 'ok') or (option.lower() == 'okay'):
        quest()
    elif option.lower() == 'n' or option.lower() == 'no' or option.lower() == 'nope':
        start1()
    else:
        pre_quest()

def quest():
    option = input(' ')
    start1()

def explore():
    explr = ['You see weird colors on the rocks', 'The sky is a unique color today!', 'The trees are there as far as I can see', 'The great hall looks great as always']
    exploreWhat = random.choice(explr)
    print(exploreWhat)
    if exploreWhat == 'You see weird colors on the rocks':
        print('1) Inspect')
        print('2) Investigate')
        print('b) Go Back')
        option = input('-> ')
        if option.lower() == 'Inspect' or option == '1':
            print('1) Touch')
            print('2) Taste')
            print('3) Smell')
        elif option.lower() == 'Investigate' or option == '2':
            print("You investigate the rock and ask people about it. People say they don't know but one of them says that he knows!")
            pre_quest(quests='Follow the purple marks on the rocks, they will lead you to a secret')
        elif option.lower() == 'back' or option == 'b':
            start1()
    else:
        print('1) Keep Exploring')
        print('2) Go back')
        option = input('-> ')
        if option == '1':
            explore()
        elif option == '2':
            start1()
        else:
            print("Sorry, didn't get it!")
            print('Continue to return to start')
            option = input(' ')
            start1()

if __name__ == "__main__": 
    main()