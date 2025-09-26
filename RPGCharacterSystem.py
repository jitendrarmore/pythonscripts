# Mini Project: RPG Character System

class Character:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self):
        print(f"{self.name} attacks with a basic strike.")


class Warrior(Character):
    def attack(self):
        print(f"{self.name} swings a sword with strength level {self.level}!")


class Mage(Character):
    def attack(self):
        print(f"{self.name} casts a fireball with power level {self.level}!")


c1 = Character('SuperMan', 5)
c2 = Warrior('Thor', 10)
c3 = Mage('BatMan', 15)


c1.attack()
c2.attack()
c3.attack()

