import random


class BasicUnit:

    def __init__(self):
        self.hp = 1
        self.attack = 1
        self.protection = 1
        self.critical_damage = 1
        self.chance_critical_damage = 1

    def get_info(self):
        print("HP:", self.hp)
        print("Attack:", self.attack)
        print("Protection:", self.protection)
        print("Critical Damage:", self.critical_damage)
        print("Chance critical damage:", self.chance_critical_damage)

    def __eq__(self, other: "BasicUnit"):
        return self.hp == other.hp

    def __lt__(self, other: "BasicUnit"):
        return self.hp < other.hp

    def __gt__(self, other: "BasicUnit"):
        return self.hp > other.hp


class UnitBowman(BasicUnit):
    hp = 29
    attack = 8
    protection = 1.5
    critical_damage = 1.1
    chance_critical_damage = 0.1

    def kick(self, enemy):
        chance_critical_damage = random.random() > 0.1
        if chance_critical_damage >= 0.1:
            enemy.hp -= self.attack * self.critical_damage
        else:
            enemy.hp -= self.attack

    def unit_protection(self, enemy):
        self.hp -= (enemy.attack - self.protection)

    def status(self):
        print(self.hp)


class UnitSwordsman(BasicUnit):
    hp = 30
    attack = 2
    protection = 2
    critical_damage = 1.6
    chance_critical_damage = 0.9

    def kick(self, enemy):
        chance_critical_damage = random.random() > 0.9
        if chance_critical_damage >= 0.9:
            enemy.hp -= self.attack * self.critical_damage
        else:
            enemy.hp -= self.attack

    def unit_protection(self, enemy):
        self.hp -= (enemy.attack - self.protection)

    def status(self):
        print(self.hp)


class UnitMagician(BasicUnit):
    hp = 31
    attack = 6
    protection = 2.2
    critical_damage = 1.5
    chance_critical_damage = 0.4

    def kick(self, enemy):
        chance_critical_damage = random.random() > 0.4
        if chance_critical_damage >= 0.4:
            enemy.hp -= self.attack * self.critical_damage
        else:
            enemy.hp -= self.attack

    def unit_protection(self, enemy):
        self.hp -= (enemy.attack - self.protection)

    def status(self):
        return self.hp


class Fighting:
    def do_kick(self, hero, enemy):
        while hero.hp > 0 and enemy.hp > 0:
            hero.kick(enemy)
            enemy.unit_protection(hero)
            if enemy.hp <= 0:
                print('%s win' % hero)
            else:
                enemy.kick(hero)
                hero.unit_protection(enemy)
            if hero.hp <= 0:
                print('%s win' % enemy)
                continue
