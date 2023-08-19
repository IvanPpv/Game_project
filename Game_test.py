from Game import Swordsman, Magician

character1 = Swordsman("Jack", 50, 50, 65)
character2 = Magician("John", 50, 50, 65)
character3 = Magician("Walter", 50, 80, 20)
print(character3 == character2)
character2.get_info()
character2.arena_fight(character1)
