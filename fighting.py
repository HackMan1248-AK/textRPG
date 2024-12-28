import os, random

def fight(player, enemy):
    while True:
        os.system('cls')
        print(f'{player.name} \t\t vs \t\t {enemy.name}')
        print(f"{player.name}'s Health: {player.health}/{player.maxHealth} \t {enemy.name}'s Health: {enemy.health}/{enemy.maxHealth}")
        print(f'Potions: {player.pots}')
        print('1) Attack')
        print('2) Drink Potion')
        print('3) Run')
        option = input('>>> ')
        if option == '1':
            if attack(player, enemy): return
        elif option == '2':
            drink_potion(player)
        elif option == '3':
            run(player, enemy)
            return

def attack(player, enemy):
    os.system('cls')
    PAttack = random.randint(player.attack // 2, player.attack)
    EAttack = random.randint(enemy.attack // 2, enemy.attack)
    if PAttack == player.attack // 2:
        print('You miss')
    else:
        enemy.health -= PAttack
        print(f'You deal {PAttack} damage!')
    input(' ')
    if enemy.health <= 0:
        win(player, enemy)
        return True
    os.system('cls')
    if EAttack == enemy.attack // 2:
        print(f'The {enemy.name} missed')
    else:
        dd = EAttack * 2 - player.defense // 2
        if dd >= 0:
            player.health -= EAttack * 2 - player.defense // 2
        print(f'The {enemy.name} deals {EAttack * 2 - player.defense // 2} damage!')
    input(' ')
    if player.health <= 0:
        dead()
    return False

def drink_potion(player):
    os.system('cls')
    if player.pots == 0:
        print("You don't have any potions!")
    else:
        player.health += 50
        player.pots -= 1
        if player.health > player.maxHealth:
            player.health = player.maxHealth
        print(f'You drank a potion! You now have {player.pots} potions.')
    input(' ')

def run(player, enemy):
    os.system('cls')
    run_num = random.randint(1, 3)
    if run_num == 1:
        print('You have succesfully ran away!')
        input(' ')
    else:
        print('You failed to get away!')
        input(' ')
        os.system('cls')
        EAttack = random.randint(enemy.attack // 2, enemy.attack)
        if EAttack == enemy.attack // 2:
            print(f'The {enemy.name} missed')
        else:
            player.health -= EAttack * 6 - player.defense
            print(f'The {enemy.name} deals {EAttack * 6 - player.defense} damage!')
        input(' ')
        if player.health <= 0:
            dead()

def win(player, enemy):
    os.system('cls')
    enemy.health = enemy.maxHealth
    player.gold += enemy.gold
    print(f'You have defeated the {enemy.name}')
    print(f'{enemy.name} dropped {enemy.gold} gold!')
    potionPossibility = random.randint(1, 2)
    if potionPossibility == '1':
        print(f'{enemy.name} also dropped a potion! You now have {player.pots} potions.')
    input(' ')

def dead():
    os.system('cls')
    print('You died a heroic death!')
    input(' ')
