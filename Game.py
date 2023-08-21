class CharacterUnit:
    def __init__(self, protection, critical_damage, chance_critical_damage, hp, attack):
        self.protection = protection
        self.critical_damage = critical_damage
        self.chance_critical_damage = chance_critical_damage
        self.hp = hp
        self.attack = attack

    def get_info(self):
        print("HP:", self.hp)
        print("Attack:", self.attack)
        print("Protection:", self.protection)
        print("Critical Damage:", self.critical_damage)
        print("Chance critical damage:", self.chance_critical_damage)

    def __eq__(self, other: "CharacterUnit"):
        return self.hp == other.hp

    def __lt__(self, other: "CharacterUnit"):
        return self.hp < other.hp

    def __gt__(self, other: "CharacterUnit"):
        return self.hp > other.hp

    def arena_fight(self, enemy):
        while self.hp > 0 and enemy.hp > 0:
            self.fight(enemy)
            if enemy.hp > 0:
                enemy.fight(self)

            if self.hp <= 0:
                print(f'{self} dead, {enemy} winner')
            elif enemy.hp <= 0:
                print(f'{enemy} dead, {self} winner')

    def fight(self, enemy):
        enemy.hp = enemy.hp - self.attack


class Swordsman(CharacterUnit):
    def __init__(self, protection = 50, critical_damage = 12, chance_critical_damage = 50, hp = 120, attack = 10):
        super().__init__(protection, critical_damage, chance_critical_damage, hp, attack)


class Bowman(CharacterUnit):
    def __init__(self, protection = 55, critical_damage = 11, chance_critical_damage = 60, hp = 100, attack = 11):
        super().__init__(protection, critical_damage, chance_critical_damage, hp, attack)


class Magician(CharacterUnit):
    def __init__(self, protection = 60, critical_damage = 14, chance_critical_damage = 70, hp = 110, attack = 13):
        super().__init__(protection, critical_damage, chance_critical_damage, hp, attack)
