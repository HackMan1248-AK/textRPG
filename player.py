class Player:
    def __init__(self, name):
        self.name = name
        self.bossFightHealth = 250
        self.maxHealth = 100
        self.health = self.maxHealth
        self.base_attack = 10
        self.base_defense = 10
        self.gold = 25
        self.pots = 5
        self.weapon = ['Rusty Sword']
        self.armor = ['Iron Armour']
        self.current_weapon= 'Rusty Sword'
        self.current_armor = 'Iron Armour'
        self.quests_accepted = []
        self.quests_completed = []

    @property
    def attack(self):
        attack = self.base_attack
        if self.current_weapon== 'Rusty Sword':
            attack += 5
        if self.current_weapon== 'Great Sword':
            attack += 15
        return attack

    @property
    def defense(self):
        defense = self.base_defense
        if self.current_armor== 'Iron Armour':
            defense += 5
        if self.current_armor== 'Platinum Armour':
            defense += 15
        return defense