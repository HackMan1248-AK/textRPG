import random

class Enemy:
    def __init__(self, name, maxHealth, attack, defense, gold, attacks=None):
        self.name = name
        self.maxHealth = maxHealth
        self.health = self.maxHealth
        self.attack = attack
        self.defense = defense
        self.gold = gold
        self.attacks = attacks
    
    def fight(self, player):
        if self.attacks == None:
            EAttack = random.randint(self.attack // 2, self.attack)
            if EAttack <= self.attack // 2:
                print(f'The {self.name} missed')
            else:
                dd = EAttack * 2 - player.defense // 2
                if dd >= 0:
                    player.health -= EAttack * 2 - player.defense // 2
                print(f'The {self.name} deals {EAttack * 2 - player.defense // 2} damage!')

        else:
            # The dictionary is ["name of attack": first two digits are damage last digit is chance of attack]
            attack = random.choices(list(self.attacks.keys()), weights=[self.attacks[item] % 10 for item in self.attacks], k=1)[0]
            EAttack = random.randint(self.attacks[attack] // 10 // 2, self.attacks[attack] // 10)
            if EAttack <= self.attacks[attack] // 10 // 2:
                print(f'The {self.name} missed')
            else:
                dd = EAttack * 2 - player.defense // 2
                if dd >= 0:
                    player.health -= EAttack * 2 - player.defense // 2
                print(f'The {self.name} used {attack} and dealt {EAttack * 2 - player.defense // 2} damage!')