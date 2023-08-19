class Swordsman:
    def __init__(self, name, protection, critical_damage, chance_critical_damage):
        self.name = name
        self.protection = protection
        self.critical_damage = critical_damage
        self.chance_critical_damage = chance_critical_damage
        self.hp = 100
        self.attack = 10

    def get_info(self):
        print("Name:", self.name)
        print("HP:", self.hp)
        print("Attack:", self.attack)
        print("Protection:", self.protection)
        print("Critical Damage:", self.critical_damage)
        print("Chance critical damage:", self.chance_critical_damage)

    def __eq__(self, other: "Swordsman"):
        return self.hp == other.hp

    def __lt__(self, other: "Swordsman"):
        return self.hp < other.hp

    def __gt__(self, other: "Swordsman"):
        return self.hp > other.hp

    def fight(self, enemy):
        enemy.hp = enemy.hp - self.attack

    def arena_fight(self, enemy):
        while self.hp > 0 and enemy.hp > 0:
            self.fight(enemy)
            if enemy.hp > 0:
                enemy.fight(self)

            if self.hp <= 0:
                print(f'{self.name} dead, {enemy.name} winner')
            elif enemy.hp <= 0:
                print(f'{enemy.name} dead, {self.name} winner')


class Bowman:
    def __init__(self, name, protection, critical_damage, chance_critical_damage):
        self.name = name
        self.protection = protection
        self.critical_damage = critical_damage
        self.chance_critical_damage = chance_critical_damage
        self.hp = 110
        self.attack = 9

    def get_info(self):
        print("Name:", self.name)
        print("HP:", self.hp)
        print("Attack:", self.attack)
        print("Protection:", self.protection)
        print("Critical Damage:", self.critical_damage)
        print("Chance critical damage:", self.chance_critical_damage)

    def __eq__(self, other: "Bowman"):
        return self.hp == other.hp

    def __lt__(self, other: "Bowman"):
        return self.hp < other.hp

    def __gt__(self, other: "Bowman"):
        return self.hp > other.hp

    def fight(self, enemy):
        enemy.hp = enemy.hp - self.attack

    def arena_fight(self, enemy):
        while self.hp > 0 and enemy.hp > 0:
            self.fight(enemy)
            if enemy.hp > 0:
                enemy.fight(self)

            if self.hp <= 0:
                print(f'{self.name} dead, {enemy.name} winner')
            elif enemy.hp <= 0:
                print(f'{enemy.name} dead, {self.name} winner')


class Magician:
    def __init__(self, name, protection, critical_damage, chance_critical_damage):
        self.name = name
        self.protection = protection
        self.critical_damage = critical_damage
        self.chance_critical_damage = chance_critical_damage
        self.hp = 120
        self.attack = 8

    def get_info(self):
        print("Name:", self.name)
        print("HP:", self.hp)
        print("Attack:", self.attack)
        print("Protection:", self.protection)
        print("Critical Damage:", self.critical_damage)
        print("Chance critical damage:", self.chance_critical_damage)

    def __eq__(self, other: "Magician"):
        return self.hp == other.hp

    def __lt__(self, other: "Magician"):
        return self.hp < other.hp

    def __gt__(self, other: "Magician"):
        return self.hp > other.hp

    def fight(self, enemy):
        enemy.hp = enemy.hp - self.attack

    def arena_fight(self, enemy):
        while self.hp > 0 and enemy.hp > 0:
            self.fight(enemy)
            if enemy.hp > 0:
                enemy.fight(self)

            if self.hp <= 0:
                print(f'{self.name} dead, {enemy.name} winner')
            elif enemy.hp <= 0:
                print(f'{enemy.name} dead, {self.name} winner')
