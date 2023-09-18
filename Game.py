class CharacterUnit:
    hp = 20
    attack = 5
    protection = 10
    critical_damage = 7
    chance_critical_damage = 5

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
    hp = 20
    attack = 5
    protection = 10
    critical_damage = 7
    chance_critical_damage = 5

    def __init__(self):
        super().__init__()


class Bowman(CharacterUnit):
    hp = 19
    attack = 4
    protection = 10
    critical_damage = 6
    chance_critical_damage = 0.6

    def __init__(self):
        super().__init__()


class Magician(CharacterUnit):
    hp = 21
    attack = 6
    protection = 12
    critical_damage = 4
    chance_critical_damage = 0.8

    def __init__(self):
        super().__init__()
