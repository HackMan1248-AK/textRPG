class Enemy:
    def __init__(self, name, maxHealth, attack, defense, gold, attacks=None):
        self.name = name
        self.maxHealth = maxHealth
        self.health = self.maxHealth
        self.attack = attack
        self.defense = defense
        self.gold = gold
        if attacks != None: self.attacks = attacks